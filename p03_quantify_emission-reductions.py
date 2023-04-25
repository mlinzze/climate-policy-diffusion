#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy
import itertools

import numpy as np
import pandas as pd

## ========================================================================================================== ##

EFFECT_SIZE = 0.01
SAMPLE = 'merged'
FIRSTYEAR = 2021
LASTYEAR = 2050

# comment out two of the three folders
IPATH = './simulations/results_mix_nonlinear_future_current/'
SENSITIVITY = True

#IPATH = './simulations/results_igo_nonlinear_future_current/'
#SENSITIVITY = False

#IPATH = './simulations/results_grv_nonlinear_future_current/'
#SENSITIVITY = False

## ============================

sample = list(pd.read_csv('./sample_{0:s}.csv'.format(SAMPLE)).iloc[:, 0].values)

sample_price = pd.read_csv('./simulations/data_P_future.csv', names=['year', 'iso', 'price']).\
				groupby('iso')['price'].max()
sample_price = sample_price[sample_price == 1].index.values

g20 = ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUE', 'FRA', 'GBR', 'IDN', 'IND',
			'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF']

## ============================

df_ghg = pd.read_csv('./data/ghg_emissions.csv')
df_ghg = df_ghg.loc[:, ['iso', 'year', 'emissions']] # in Giga tons
df_ghg = df_ghg.loc[df_ghg['iso'].isin(sample), :]
countries = df_ghg['iso'].unique()

df_ghg = df_ghg.sort_values(by=['iso', 'year'], ascending=True, ignore_index=True)
df_ghg['growth'] = 1. + (df_ghg['emissions'] - df_ghg.groupby('iso')['emissions'].shift(1)) / df_ghg.groupby('iso')['emissions'].shift(1)
df_ghg['growth_treated'] = df_ghg['growth'] - EFFECT_SIZE
df_ghg = df_ghg.loc[df_ghg['year'] >= FIRSTYEAR, :]
df_ghg = df_ghg.sort_values(by=['iso', 'year'], ascending=True).reset_index(drop=True)
df_ghg = df_ghg.set_index(['iso', 'year'])

## ============================

df = pd.read_csv(os.path.join(IPATH, 'result_{0:s}_{1:d}.csv'.format('ANY', 0)), names=['year', 'iso', 'control'])

for iso in sample:
	df1 = pd.read_csv(os.path.join(IPATH, 'result_{0:s}_{1:d}.csv'.format(iso, 1)), names=['year', 'iso', iso])
	df = df.merge(df1, on=['iso', 'year'])

df = df.loc[df['iso'].isin(countries), :]
df = df.loc[df['year'].between(FIRSTYEAR, LASTYEAR), :]
df = df.sort_values(by=['iso', 'year'], ascending=True).reset_index(drop=True)
df = df.set_index(['iso', 'year'])

## ============================

for year in range(FIRSTYEAR, LASTYEAR, 1):

	print(year)
	index = df_ghg.index.get_level_values('year') == year
	df_ghg['emissions_baseline'] = np.nan
	df_ghg.loc[index, 'emissions_baseline'] = df_ghg.loc[index, 'emissions']
	df_ghg['emissions_baseline'] = df_ghg.groupby('iso')['emissions_baseline'].ffill()
	df_ghg.loc[index, 'growth_treated_cumulative'] = 1.

	index = df_ghg.index.get_level_values('year') > year
	df_ghg.loc[index, 'growth_treated_cumulative'] = df_ghg.loc[index, :].groupby('iso')['growth_treated'].transform(lambda x: x.cumprod())
	df_ghg['emissions_treated'] = df_ghg['emissions_baseline'] * df_ghg['growth_treated_cumulative']

	reductions = df_ghg.loc[index, :].groupby('iso')['emissions'].sum() - df_ghg.loc[index, :].groupby('iso')['emissions_treated'].sum()

	index = df.index.get_level_values('year') == year
	df.loc[index, :] = df.loc[index, :].multiply(reductions.values, axis='index')

df_results = pd.DataFrame({'iso': countries})
df_results = df_results.set_index('iso')

for iso in countries:

	df_results.loc[iso, 'direct'] = df.loc[df.index.get_level_values('iso') == iso, iso].sum(axis=0)
	df_results.loc[iso, 'indirect'] = df.loc[df.index.get_level_values('iso') != iso, iso].sum(axis=0) -\
										df.loc[df.index.get_level_values('iso') != iso, 'control'].sum(axis=0)

df_results.loc[sample_price, 'indirect'] = np.nan

df_results.to_csv(os.path.join(IPATH, 'emission_reductions.csv'))

## ========================================================================================================== ##

if SENSITIVITY == True:

	IPATH = './simulations/results_mix_nonlinear_future_current/'
	SAMPLE = 'merged'
	FIRSTYEAR = 2021
	LASTYEAR = 2050

	## ============================

	sample = list(pd.read_csv('./sample_{0:s}.csv'.format(SAMPLE)).iloc[:, 0].values)

	g20 = ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'EUE', 'FRA', 'GBR', 'IDN', 'IND',
				'ITA', 'JPN', 'KOR', 'MEX', 'RUS', 'SAU', 'TUR', 'USA', 'ZAF']

	## ============================

	for EFFECT_SIZE in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1]:

		df_ghg = pd.read_csv('./data/ghg_emissions.csv')
		df_ghg = df_ghg.loc[:, ['iso', 'year', 'emissions']] # in Giga tons
		df_ghg = df_ghg.loc[df_ghg['iso'].isin(sample), :]

		df_ghg = df_ghg.sort_values(by=['iso', 'year'], ascending=True, ignore_index=True)
		df_ghg['growth'] = 1. + (df_ghg['emissions'] - df_ghg.groupby('iso')['emissions'].shift(1)) / df_ghg.groupby('iso')['emissions'].shift(1)
		df_ghg['growth_treated'] = df_ghg['growth'] - EFFECT_SIZE
		df_ghg = df_ghg.loc[df_ghg['year'] >= FIRSTYEAR, :]
		df_ghg = df_ghg.sort_values(by=['iso', 'year'], ascending=True).reset_index(drop=True)
		df_ghg = df_ghg.set_index(['iso', 'year'])

		## ============================

		df = pd.read_csv(os.path.join(IPATH, 'result_{0:s}_{1:d}.csv'.format('ANY', 0)), names=['year', 'iso', 'control'])

		for iso in sample:
			df1 = pd.read_csv(os.path.join(IPATH, 'result_{0:s}_{1:d}.csv'.format(iso, 1)), names=['year', 'iso', iso])
			df = df.merge(df1, on=['iso', 'year'])

		df = df.loc[df['iso'].isin(countries), :]
		df = df.loc[df['year'].between(FIRSTYEAR, LASTYEAR), :]
		df = df.sort_values(by=['iso', 'year'], ascending=True).reset_index(drop=True)
		df = df.set_index(['iso', 'year'])

		## ============================

		for year in range(FIRSTYEAR, LASTYEAR, 1):

			print(year)
			index = df_ghg.index.get_level_values('year') == year
			df_ghg['emissions_baseline'] = np.nan
			df_ghg.loc[index, 'emissions_baseline'] = df_ghg.loc[index, 'emissions']
			df_ghg['emissions_baseline'] = df_ghg.groupby('iso')['emissions_baseline'].ffill()
			df_ghg.loc[index, 'growth_treated_cumulative'] = 1.

			index = df_ghg.index.get_level_values('year') > year
			df_ghg.loc[index, 'growth_treated_cumulative'] = df_ghg.loc[index, :].groupby('iso')['growth_treated'].transform(lambda x: x.cumprod())
			df_ghg['emissions_treated'] = df_ghg['emissions_baseline'] * df_ghg['growth_treated_cumulative']

			reductions = df_ghg.loc[index, :].groupby('iso')['emissions'].sum() - df_ghg.loc[index, :].groupby('iso')['emissions_treated'].sum()

			index = df.index.get_level_values('year') == year
			df.loc[index, :] = df.loc[index, :].multiply(reductions.values, axis='index')

		df_results = pd.DataFrame({'iso': countries})
		df_results = df_results.set_index('iso')

		for iso in countries:

			df_results.loc[iso, 'direct'] = df.loc[df.index.get_level_values('iso') == iso, iso].sum(axis=0)
			df_results.loc[iso, 'indirect'] = df.loc[df.index.get_level_values('iso') != iso, iso].sum(axis=0) -\
												df.loc[df.index.get_level_values('iso') != iso, 'control'].sum(axis=0)
		df_results.loc[sample_price, 'indirect'] = np.nan

		df_results.to_csv(os.path.join(IPATH, 'emission_reductions_effectsize_{0:4.3f}.csv'.format(EFFECT_SIZE)))
