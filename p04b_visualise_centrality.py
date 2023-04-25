#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from copy import deepcopy

import numpy as np
import pandas as pd

import networkx as nx
import statsmodels.api as sm

import matplotlib.pyplot as plt
import seaborn as sns

## ============================================================

YEAR = 2021

## ============================================================

df = pd.read_csv('./data/metrics.csv')

## ===============

sample = list(pd.read_csv('./sample_merged.csv').iloc[:, 0].values)
df = df.loc[df['iso1'].isin(sample) & df['iso2'].isin(sample), :]
df = df.loc[df['iso1'] != df['iso2'], :]

## ===============

df['proximity_gdp_igo'] = df['proximity_gdp_igo'] / df.groupby(['iso1', 'year'])['proximity_gdp_igo'].transform(lambda x: x.sum())
df['index'] = df.index.values

## ============================================================

df_year = df.loc[df['year'] == YEAR, :]

## ===============

df_ghg = pd.read_csv('./data/ghg_emissions.csv')
df_ghg = df_ghg.loc[:, ['iso', 'year', 'emissions']]
df_ghg = df_ghg.loc[df_ghg['iso'].isin(sample) & (df_ghg['year'] == YEAR), :]
df_year = df_year.merge(df_ghg, left_on=['iso1', 'year'], right_on=['iso', 'year'])
df_year['weight'] = df_year['proximity_gdp_igo'] * df_year['emissions']

## ===============

a = df_year.groupby('iso2')['proximity_gdp_igo'].sum()
b = df_year.groupby('iso2')['weight'].sum()
countries = df_year['iso1'].unique()
m = pd.DataFrame(index=countries)
for iso in countries:
	n = df_year.loc[df_year['iso1'] != iso, :].groupby('iso2')['weight'].sum()
	n.name = iso
	m = m.merge(n, left_index=True, right_index=True, how='left')
mm = m.reset_index().melt(id_vars=['index'], value_vars=m.columns, var_name='iso2', value_name='c')
mm = mm.rename(columns={'index': 'iso1'})
df_year = df_year.merge(mm, left_on=['iso1', 'iso2'], right_on=['iso1', 'iso2'], how='left')
df_year['d'] = df_year['proximity_gdp_igo'] * df_year['c']
d = df_year.groupby('iso2')['d'].sum()
a.name = 'a'
b.name = 'b'
d.name = 'd'
df_centrality = pd.concat([a, b, d], axis=1)

df_centrality['bd'] = df_centrality['b'] + df_centrality['d']

## ===============

dfe = pd.read_csv('./simulations/results_mix_nonlinear_future_current/emission_reductions.csv')
df_centrality = df_centrality.merge(dfe, left_on='iso2', right_on='iso', how='right')

df_centrality.corr().loc[['a', 'b', 'd'], :]

## ===============

formula = 'indirect ~ a'
res = sm.OLS.from_formula(formula=formula, data=df_centrality).fit(missing='drop').get_robustcov_results()
dx = res.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]
print(res.rsquared)

formula = 'indirect ~ b'
res = sm.OLS.from_formula(formula=formula, data=df_centrality).fit(missing='drop').get_robustcov_results()
dx = res.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]
print(res.rsquared)

formula = 'indirect ~ d'
res = sm.OLS.from_formula(formula=formula, data=df_centrality).fit(missing='drop').get_robustcov_results()
dx = res.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]
print(res.rsquared)

## ===============

df_centrality = df_centrality.set_index('iso')

## ================

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_centrality.index.values:
	x = df_centrality.loc[iso, 'd']
	y = df_centrality.loc[iso, 'indirect']
	ax.plot(x, y, color='white')
	ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data',
			ha='center', va='center', size='small', color='black', alpha=0.2)
ax.annotate(text='Correlation: {0:3.2f}'.format(\
		df_centrality.corr().loc['d', 'indirect']),
		xy=(0.05, 0.99), xycoords='axes fraction',
		ha='left', va='top', size='small', color='black', alpha=1.)
ax.set_xlabel('Network centrality\n (direct and indirect influences)')
ax.set_ylabel('Indirect emission reductions (Gt)')
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_centrality_labels.pdf', bbox_inches='tight', transparent=True)

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_centrality.index.values:
	x = df_centrality.loc[iso, 'b']
	y = df_centrality.loc[iso, 'indirect']
	ax.plot(x, y, color='white')
	ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data',
			ha='center', va='center', size='small', color='black', alpha=0.2)
ax.annotate(text='Correlation: {0:3.2f}'.format(\
		df_centrality.corr().loc['b', 'indirect']),
		xy=(0.05, 0.99), xycoords='axes fraction',
		ha='left', va='top', size='small', color='black', alpha=1.)
ax.set_xlabel('Network centrality\n (only direct influences)')
ax.set_ylabel('Indirect emission reductions (Gt)')
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_centrality_labels_direct.pdf', bbox_inches='tight', transparent=True)

## ============================================================

def metrics(df):
	a = df.groupby('iso2')['proximity_gdp_igo'].sum()
	b = df.groupby('iso2')['weight'].sum()
	countries = df['iso1'].unique()
	m = pd.DataFrame(index=countries)
	for iso in countries:
		n = df.loc[df['iso1'] != iso, :].groupby('iso2')['weight'].sum()
		n.name = iso
		m = m.merge(n, left_index=True, right_index=True, how='left')
	mm = m.reset_index().melt(id_vars=['index'], value_vars=m.columns, var_name='iso2', value_name='c')
	mm = mm.rename(columns={'index': 'iso1'})
	df = df.merge(mm, left_on=['iso1', 'iso2'], right_on=['iso1', 'iso2'], how='left')
	df['d'] = df['proximity_gdp_igo'] * df['c']
	d = df.groupby('iso2')['d'].sum()
	a.name = 'a'
	b.name = 'b'
	d.name = 'd'
	abd = pd.concat([a, b, d], axis=1).reset_index()
	return abd

years = range(1988, 2022+1, 1)
df_results = pd.DataFrame()

for year in years:

	df_year = df.loc[df['year'] == year, :]
	df_year = df_year.merge(df_ghg, left_on='iso1', right_on='iso')
	df_year['weight'] = df_year['proximity_gdp_igo'] * df_year['emissions']
	res = metrics(df_year)
	res['year'] = year
	df_results = pd.concat([df_results, res], axis=0)

y1 = df_results.loc[df_results['year'] == 1990, :]
y2 = df_results.loc[df_results['year'] == 2020, :]

print(y1['a'].std(), y2['a'].std())
print(y1['b'].std(), y2['b'].std())
print(y1['d'].std(), y2['d'].std())

bins = np.arange(0., 0.5+0.025, 0.025)

fig, ax = plt.subplots(figsize=(5,4))
ax.hist(y1['d'], bins=bins, density=True, alpha=0.2, color='b')#, label='1990')
ax.hist(y2['d'], bins=bins, density=True, alpha=0.2, color='r')#, label='2020')
sns.kdeplot(data=y1, x='d', color='b', label='1990', ax=ax)
sns.kdeplot(data=y2, x='d', color='r', label='2020', ax=ax, linestyle='--')
ax.set_xlabel('Network centrality\n (direct and indirect influences)')
ax.set_ylabel('Density of countries')
ax.legend()
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/histogram_centrality.pdf', bbox_inches='tight', transparent=True)

fig, ax = plt.subplots(figsize=(5,4))
ax.hist(y1['b'], bins=bins, density=True, alpha=0.2, color='b')#, label='1990')
ax.hist(y2['b'], bins=bins, density=True, alpha=0.2, color='r')#, label='2020')
sns.kdeplot(data=y1, x='b', color='b', label='1990', ax=ax)
sns.kdeplot(data=y2, x='b', color='r', label='2020', ax=ax, linestyle='--')
ax.set_xlabel('Network centrality\n (only direct influences)')
ax.set_ylabel('Density of countries')
ax.legend()
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/histogram_centrality_direct.pdf', bbox_inches='tight', transparent=True)
