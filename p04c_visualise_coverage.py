#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy
import itertools

import numpy as np
import pandas as pd
import random
import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
	new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
		'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
		cmap(np.linspace(minval, maxval, n)))
	return new_cmap

cmap = truncate_colormap(plt.cm.Greens, minval=0.2, maxval=1.)
cmap.set_under('grey')
try:
	mpl.cm.register_cmap("custom_cmap", cmap)
except:
	pass

## ============================

EXPERIMENT = 'mix_nonlinear_future_current'

sample = list(pd.read_csv('./sample_{0:s}.csv'.format('merged')).iloc[:, 0].values)

g20 = ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUE', 'FRA', 'GBR', 'IDN', 'IND',
			'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF']

sample_price = pd.read_csv('./simulations/data_P_future.csv', names=['year', 'iso', 'price']).\
				groupby('iso')['price'].max()
sample_price = sample_price[sample_price == 1].index.values

## ============================

baseline_factors = [0.5, 0.75, 1., 1.25, 1.5, 1.75, 2.]
diffusion_factors = [0.5, 0.75, 1., 1.25, 1.5, 1.75, 2.]

n_baseline = len(baseline_factors)
n_diffusion = len(diffusion_factors)

df_all = pd.DataFrame()

for diffusion in [0, 1]:
	for i1 in range(0, n_baseline, 1):
		for i2 in range(0, n_diffusion, 1):

			df = pd.read_csv('./simulations/results_{0:s}/result_ANY_{1:d}_b{2:d}_d{3:d}.csv'.format(\
								EXPERIMENT, diffusion, i1, i2),
								names=['year', 'iso', 'P'])
			df['baseline_factor'] = baseline_factors[i1]
			df['diffusion_factor'] = diffusion_factors[i2]
			df['diffusion'] = diffusion
			df_all = pd.concat([df_all, df], axis=0)

df_all['P'] = df_all.groupby(['diffusion', 'baseline_factor', 'diffusion_factor', 'iso'])['P'].transform(lambda x: x.cumsum())


df_ghg = pd.read_csv('./data/ghg_emissions.csv')
df_ghg = df_ghg.loc[df_ghg['iso'].isin(sample), :]
df_ghg = df_ghg.loc[df_ghg['year'] == 2022, :]
df_ghg = df_ghg.loc[:, ['iso', 'emissions']] # in Giga tons
emissions_total = df_ghg['emissions'].sum()

df_all = df_all.merge(df_ghg, on='iso', how='left')
df_all['E'] = df_all['P'] * df_all['emissions'] / emissions_total

dfe = df_all.groupby(['diffusion', 'baseline_factor', 'diffusion_factor', 'year'])['P'].sum().reset_index()
dfe['E'] = df_all.groupby(['diffusion', 'baseline_factor', 'diffusion_factor', 'year'])['E'].sum().reset_index()['E'].values
df_all = dfe

df_all['P'] = df_all['P'] / 188.

df_all = df_all.pivot_table(index=['baseline_factor', 'diffusion_factor', 'year'],
							values=['P', 'E'], columns=['diffusion']).reset_index()
df_all.columns = [i[0] for i in list(df_all.columns[:-4])] + ['E0', 'E1'] + ['P0', 'P1']
df_all['Pd'] = df_all['P1'] - df_all['P0']
df_all['Ed'] = df_all['E1'] - df_all['E0']

## ============================

dfm = df_all.loc[df_all['year'] == 2050, :]
dfm['label'] = dfm['P1'].apply(lambda x: '{0:2.0f}\n'.format(x*100)) + \
				dfm['Pd'].apply(lambda x: '({0:+2.0f})'.format(x*100))

def plotlabel(xvar, yvar, label, color='k'):
	ax.text(xvar, yvar, label, ha='center', va='center', size='large', color=color)

fig, ax = plt.subplots(figsize=(6,5))
sns.scatterplot(ax=ax, data=dfm, x='baseline_factor', y='diffusion_factor', hue='P1',
		palette=cmap, legend=False, s=1500)
dfm.loc[dfm['P1'] < 0.6, :].apply(lambda x: plotlabel(x['baseline_factor'], x['diffusion_factor'], x['label'], color='k'), axis=1)
dfm.loc[dfm['P1'] >= 0.6, :].apply(lambda x: plotlabel(x['baseline_factor'], x['diffusion_factor'], x['label'], color='w'), axis=1)
ax.plot(1., 1., marker='s', markersize=40, markeredgecolor='r', markerfacecolor='none')
ax.set_xlabel('Baseline hazard\n(relative to estimate)')
ax.set_ylabel('Diffusion parameter\n(relative to estimate)')
ax.set_xlim(0.38, 2.12)
ax.set_ylim(0.38, 2.12)
ax.set_xticks(np.arange(0.5, 2.+0.25, 0.25))
ax.set_yticks(np.arange(0.5, 2.+0.25, 0.25))
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_sensitivity.pdf', bbox_inches='tight', dpi=300., transparent=True)

## ============================

dfm = df_all.loc[df_all['year'] == 2050, :]
dfm['label'] = dfm['E1'].apply(lambda x: '{0:2.0f}\n'.format(x*100)) + \
				dfm['Ed'].apply(lambda x: '({0:+2.0f})'.format(x*100))

def plotlabel(xvar, yvar, label, color='k'):
	ax.text(xvar, yvar, label, ha='center', va='center', size='large', color=color)

fig, ax = plt.subplots(figsize=(6,5))
ax.set_title("Global coverage of carbon pricing policies \n(% GHG emissions)\n")
sns.scatterplot(ax=ax, data=dfm, x='baseline_factor', y='diffusion_factor', hue='E1',
		palette="custom_cmap", legend=False, s=1500)
dfm.loc[dfm['E1'] < 0.8, :].apply(lambda x: plotlabel(x['baseline_factor'], x['diffusion_factor'], x['label'], color='k'), axis=1)
dfm.loc[dfm['E1'] >= 0.8, :].apply(lambda x: plotlabel(x['baseline_factor'], x['diffusion_factor'], x['label'], color='w'), axis=1)
ax.plot(1., 1., marker='s', markersize=40, markeredgecolor='r', markerfacecolor='none')
ax.set_xlabel('Baseline hazard\n(relative to estimate)')
ax.set_ylabel('Diffusion parameter\n(relative to estimate)')
ax.set_xlim(0.38, 2.12)
ax.set_ylim(0.38, 2.12)
ax.set_xticks(np.arange(0.5, 2.+0.25, 0.25))
ax.set_yticks(np.arange(0.5, 2.+0.25, 0.25))
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_sensitivity_emissions.pdf', bbox_inches='tight', dpi=300., transparent=True)

## ============================

df = pd.read_csv('./data/policies.csv')
sample = list(pd.read_csv('./sample_merged.csv').iloc[:, 0].values)
df = df.loc[df['iso'].isin(sample), :]
dfm = df.groupby(['year'])['price'].sum() / df.groupby(['year'])['price'].count()
dfm = dfm.reset_index()
dfm = dfm.loc[dfm['year'] >= 1989, :]
x0 = dfm['year'].values
y0 = dfm['price'].values

df0 = pd.read_csv('./simulations/results_mix_nonlinear_future100_current/result_ANY_0_b0_d0.csv',
					names=['year', 'iso', 'P'])
df1 = pd.read_csv('./simulations/results_mix_nonlinear_future100_current/result_ANY_1_b0_d0.csv',
					names=['year', 'iso', 'P'])
df_all = df0.merge(df1, on=['year', 'iso'], suffixes=['0', '1'])
df_all['P0'] = df_all.groupby(['iso'])['P0'].transform(lambda x: x.cumsum())
df_all['P1'] = df_all.groupby(['iso'])['P1'].transform(lambda x: x.cumsum())
df_all = df_all.groupby(['year']).sum().reset_index()
df_all['P0'] = df_all['P0'] / 188.
df_all['P1'] = df_all['P1'] / 188.

x1 = df_all['year'].values
y11 = df_all['P1'].values
y12 = df_all['P0'].values

fig, ax = plt.subplots(figsize=(6,5))
ax.plot(x0, y0, 'k-', label='1989-2021')
ax.plot(x1, y11, 'b--', label='2022-2100, with diffusion')
ax.plot(x1, y12, 'b:', label='2022-2100, without diffusion')
ax.set_xlabel('Time')
ax.set_ylabel('Share of countries with carbon price')
sns.despine(ax=ax, offset=1., right=True, top=True)
ax.set_ylim(0., 0.75)
ax.grid(axis='y')
ax.legend(loc='upper left')
ax.set_yticks(np.arange(0., 0.8, 0.1))
ax.set_yticklabels(['{0:2.0f}%'.format(i*100) for i in np.arange(0., 0.8, 0.1)])
fig.savefig('./figures/timeseries_sensitivity_extended.pdf', bbox_inches='tight', dpi=300., transparent=True)
fig.savefig('./figures/timeseries_sensitivity_extended.png', bbox_inches='tight', dpi=300., transparent=True)

## ============================

print(y11[x1 == 2050] - y12[x1 == 2050])
