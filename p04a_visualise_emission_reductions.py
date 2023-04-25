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

EXPERIMENT = 'mix_nonlinear_future_current'

g20 = ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUE', 'FRA', 'GBR', 'IDN', 'IND',
			'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF']

## ============================

sample_price = pd.read_csv('./simulations/data_P_future.csv', names=['year', 'iso', 'price']).\
				groupby('iso')['price'].max()
sample_price = sample_price[sample_price == 1].index.values

## ============================

COLOR1 = 'b'
COLOR2 = 'r'
COLOR3 = 'm'
COLOR4 = 'c'
COLOR5 = 'g'

label = EXPERIMENT

## ============================
## plot scatter
## ============================

df_results = pd.read_csv('./simulations/results_{0:s}/emission_reductions.csv'.format(EXPERIMENT))

# countries that had CP in 2020
df_results.loc[df_results['iso'].isin(sample_price), 'direct'] = np.nan
df_results.loc[df_results['iso'].isin(sample_price), 'indirect'] = np.nan

df_results['indirect_larger'] = df_results['indirect'] > df_results['direct']
df_results['factor'] = df_results['indirect'] / df_results['direct']
df_results['indirect_larger'].sum() / df_results['direct'].count()

## ============================

df_results = df_results.set_index('iso')

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_results.index.values:
	if iso == 'TUV':
		continue
	x = df_results.loc[iso, 'direct']
	y = df_results.loc[iso, 'indirect']
	ax.plot(x, y, color='white')
	if iso in g20:
		ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data', ha='center', va='center', size='small', color=COLOR1)
	else:
		ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data', ha='center', va='center', size='small', color='black', alpha=0.2)
ax.set_xlabel('Direct emission reductions (Gt CO2eq)')
ax.set_ylabel('Indirect emission red. (Gt CO2eq)')
ax.set_ylim(9e-3, 0.6)
ax.set_xscale('log')
ax.set_yscale('log')
xlims = ax.get_xlim()
ylims = ax.get_ylim()
ax.plot([0., 0.], ylims, 'k-', lw=0.5)
ax.plot(np.linspace(0., ylims[-1], 1000), np.linspace(0., ylims[-1], 1000), 'k--')
ax.set_ylim(ylims)
ax.set_xlim(xlims)
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_indirect_{0:s}.pdf'.format(EXPERIMENT), bbox_inches='tight', dpi=300., transparent=True)
fig.savefig('./figures/scatter_indirect_{0:s}.png'.format(EXPERIMENT), bbox_inches='tight', dpi=300., transparent=True)

## ============================
## plot histogram
## ============================

print((df_results['factor']>1.).sum() / df_results['factor'].count())

bins = [0.00001 * 2. ** k for k in range(0, 20, 1)]
fig, ax = plt.subplots(figsize=(5,4))
ax.hist(df_results['direct'], density=False, bins=bins, color=COLOR3, alpha=0.6, hatch='//', label='Direct emissions')
ax.hist(df_results['indirect'], density=False, bins=bins, color=COLOR5, alpha=0.6, hatch='..', label='Indirect emissions')
ax.set_ylabel('Number of countries')
ax.set_xlabel('Emission reductions (Gt CO2eq)')
ax.set_xscale('log')
ax.legend(loc='upper left')
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/histogram_emissions_{0:s}.pdf'.format(EXPERIMENT), bbox_inches='tight', dpi=300., transparent=True)

## ============================
## plot map
## ============================

# read in shapes
datapath = "./data/"
datafile = "country_geometries.shp"
gdf_countries = gpd.read_file(os.path.join(datapath, datafile))
gdf = gdf_countries.merge(df_results, left_on=['iso'], right_on=['iso'], how='left')
gdf.loc[gdf['iso'].isin(sample_price), 'price'] = True

bounds = [0., 0.05, 0.1, 0.15, 0.2, 0.25]

extend = 'both'
formatcode = '%.2f'
fig, ax = plt.subplots(figsize=(10,6))
cmap = plt.cm.Greens
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
ax2 = fig.add_axes([0.95, 0.25, 0.03, 0.5])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
	spacing='uniform', ticks=bounds, boundaries=bounds, format=formatcode, label='Indirect emission reductions (Gt)', extend=extend)#{0:s}'.format(variable.replace('_', ' before '))
gdf.plot(ax=ax, facecolor='k', alpha=0.1, ec='k', lw=0.5)
gdf.loc[gdf['price'] == True, :].plot(ax=ax, facecolor='k', alpha=0.4, ec='k', lw=0.5)
gdf.plot(ax=ax, column='indirect', cmap=cmap, norm=norm, vmin=bounds[0], vmax=bounds[-1], markersize=0.02, facecolor='k', marker='o', ec='k', lw=0.5)
ax.set_xlabel('Longitude (degrees)')
ax.set_ylabel('Latitude (degrees)')
ax.set_xlim(-130., 180.)
ax.set_ylim(-60., 75.)
fig.savefig(os.path.join('./figures', 'geomap_indirect_{0:s}.png'.format(EXPERIMENT)), bbox_inches='tight', dpi=200)

## ============================
## histogram with both metrics
## ============================

g20 = ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUE', 'FRA', 'GBR', 'IDN', 'IND',
			'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF']

## ============================
## read
## ============================

EXPERIMENT = 'grv_nonlinear_future_current'

df_results1 = pd.read_csv('./simulations/results_{0:s}/emission_reductions.csv'.format(EXPERIMENT))

df_results1.loc[df_results1['indirect'] < 0., 'indirect'] = np.nan
df_results1.loc[df_results1['direct'] < 0., 'direct'] = np.nan

# those which had CP in 2020
df_results1.loc[df_results1['direct'] == 0., 'direct'] = np.nan

df_results1['indirect_larger'] = df_results1['indirect'] > df_results1['direct']
df_results1['factor'] = df_results1['indirect'] / df_results1['direct']

## ============================

EXPERIMENT = 'igo_nonlinear_future_current'

df_results2 = pd.read_csv('./simulations/results_{0:s}/emission_reductions.csv'.format(EXPERIMENT))

df_results2.loc[df_results2['indirect'] < 0., 'indirect'] = np.nan
df_results2.loc[df_results2['direct'] < 0., 'direct'] = np.nan

# those which had CP in 2020
df_results2.loc[df_results2['direct'] == 0., 'direct'] = np.nan

df_results2['indirect_larger'] = df_results2['indirect'] > df_results2['direct']
df_results2['factor'] = df_results2['indirect'] / df_results2['direct']

plt.rcParams['hatch.color'] = 'k'

bins = np.arange(0., 0.325, 0.025)
fig, ax = plt.subplots(figsize=(5,4))
ax.hist(df_results1['indirect'], bins=bins, density=True, color=COLOR1, hatch='//', alpha=0.6, label='Gravity', zorder=1)
ax.hist(df_results2['indirect'], bins=bins, density=True, color=COLOR2, hatch='..', alpha=0.6, label='IO', zorder=2)
ax.set_ylabel('Histogram')
ax.set_xlabel('Indirect emission reductions (Gt)')
ax.legend()
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/histogram_indirect_{0:s}.pdf'.format('comparison'), bbox_inches='tight', dpi=300.)

df_results = df_results1.merge(df_results2, on=['iso'], suffixes=['_grv', '_igo'])
df_results = df_results.set_index('iso')
df_results = df_results.dropna()

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_results.index.values:
	x = df_results.loc[iso, 'indirect_grv']
	y = df_results.loc[iso, 'indirect_igo']
	ax.plot(x, y, color='white')
	ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data',
			ha='center', va='center', size='small', color='black', alpha=0.6)
ax.set_xlabel('Indirect emission reductions - Gravity (Gt)')
ax.set_ylabel('Indirect emission reductions - IO (Gt)')
ax.annotate(text='Correlation: {0:3.2f}'.format(\
		df_results.corr().loc['indirect_grv', 'indirect_igo']),
		xy=(0.05, 0.99), xycoords='axes fraction',
		ha='left', va='top', size='small', color='black', alpha=1.)
ax.set_xlim(-0.02, 0.27)
ax.set_ylim(-0.02, 0.27)
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/scatter_indirect_{0:s}.pdf'.format('comparison'), bbox_inches='tight', dpi=300.)
