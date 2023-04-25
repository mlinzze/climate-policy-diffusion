#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from copy import deepcopy

import numpy as np
import pandas as pd

from scipy.stats import t 

## ===== define some functions ===== ##

def get_stars(p, mode=1):
	if mode == 0:
		if p < 0.001:
			return '$^{* * *}$'
		elif p < 0.01:
			return '$^{* *}$'
		elif p < 0.05:
			return '$^{*}$'
		else:
			return ''
	elif mode == 1:
		if p < 0.01:
			return '$^{* * *}$'
		elif p < 0.05:
			return '$^{* *}$'
		elif p < 0.1:
			return '$^{*}$'
		else:
			return ''

def sort_variables(df, var2name):
	df['var_sort'] = df['Variable']
	categories_estimates = list(var2name.keys())
	categories_SE = [c + '_SE' for c in categories_estimates]
	categories_all = [None]*(len(categories_estimates)+len(categories_SE))
	categories_all[::2] = categories_estimates
	categories_all[1::2] = categories_SE
	df['var_sort'] = pd.Categorical(
	    df['var_sort'], 
	    categories=categories_all, 
	    ordered=True
	)
	df = df.sort_values(by='var_sort', ignore_index=True)
	df = df.drop(columns=['var_sort'])
	return df

## ===== variable names for table ===== ##

var2name = {\
			'spatial_lag': 'Spatial lag of carbon pricing',
			'spatial_lag_sq': 'Spatial lag of carbon pricing (sq)',
			'spatial_lag_tr': 'Spatial lag of carbon pricing (tr)',
			'log_gdp_pc_ppp': 'Log real GDP per capita PPP',
			'exports_share': 'Exports share of GDP',
			'imports_share': 'Imports share of GDP',
			'services_share': 'Services share of GDP',
			'industry_share': 'Industry share of GDP',
			'population': 'Population',
			'emissions_co2': 'Emissions CO2',
			'control_corruption': 'Control of corruption',
			'government_effectiveness': 'Government effectiveness',
			'regulatory_quality': 'Regulatory quality',
			'rule_of_law': 'Rule of law',
			'reserves_oil': 'Reserves of oil',
			'reserves_gas': 'Reserves of gas',
			'reserves_coal': 'Reserves of coal',
			'exposure_pm25': 'Air pollution PM2.5',
			'government_debt': 'Government debt',
			'government_expenditure': 'Government expenditure',
			'welfare': 'Gov. expendit. welfare',
			'belief': 'Public belief in climate change',
			'polity2': 'Democracy index',
			'emission_intensity': 'Emission intensity',
			'g_gdp': 'Growth rate of real GDP',
			'g_debt': 'Growth rate of debt to GDP ratio',
			'1.kyoto': 'Kyoto Annex I',
			'1.eu': 'European Union',
			'empty': '',
}

stat2name = {\
	'll': 'log-likelihood',
	'r2': 'R2',
	'p': 'p',
	'aic': 'AIC',
	'bic': 'BIC',
	'N': 'N',
	'risk': 'Time at risk'
}

## ===== create latex tables ===== ##

for TABLE_ID in ['01', '02', '03', '04', '05', '06']:

	if TABLE_ID == '01':
		EXPERIMENTS = [\
						'A01',
						'A02',
						'A03',
						]
		COLUMN_NAMES = ['main', 'tax', 'ets']
		COLUMN_NAMES = [str(i+1) for i in range(np.size(EXPERIMENTS))]

	elif TABLE_ID == '02':
		EXPERIMENTS = [\
						'B01',
						'B02',
						'B03',
						'B04',
						'B05',
						'B06',
						'B07',
						'B08',
						'B09',
						]
		COLUMN_NAMES = ['d', 'exp', 'imp', 'exp.x', 'imp.x', 'igo', 'grav', 'mix', 'rand']

	elif TABLE_ID == '03':
		EXPERIMENTS = [\
						'C01',
						'C02',
						'C03',
						'C04',
						'C05',
						'C06',
						]
		COLUMN_NAMES = ['eu ind', 'main', 'eu ets', 'national', 'lvl', 'lvl.log']

	elif TABLE_ID == '04':
		EXPERIMENTS = [\
						'D01',
						'D02',
						'D03',
						'D04',
						]
		COLUMN_NAMES = ['lasso', 'all', 'constant', 'strata']


	elif TABLE_ID == '05':
		EXPERIMENTS = [\
						'E01',
						'E02',
						'E03',
						]
		COLUMN_NAMES = ['lin', 'sq', 'tr']

	elif TABLE_ID == '06':
		EXPERIMENTS = [\
						'F01',
						'F02',
						'F03',
						'F04',
						'F05',
						]
		COLUMN_NAMES = [str(i+1) for i in range(np.size(EXPERIMENTS))]

	else:
		continue

	df_all = pd.DataFrame(columns=['Variable'])

	for i, EXPERIMENT in enumerate(EXPERIMENTS):

		df_column = pd.DataFrame()

		COLUMN_NAME = COLUMN_NAMES[i]

		# read in regression results as data frame
		datapath = './results/'
		ifile = 'coeffs_{0:s}.txt'.format(EXPERIMENT)
		with open(os.path.join(datapath, ifile), 'r') as ifp:
			ilines = ifp.readlines()

		n_columns = len(ilines[0].split('&'))
		df_coeffs = pd.DataFrame()
		for i, variable in enumerate(var2name.keys()):
			for line in ilines:
				if variable == line.split(' ')[0]:
					coeff, se, p = [float(a) for a in line.split('&')[1].split('|')]
					df_column.loc[variable, COLUMN_NAME] = '{0:5.4f}'.format(coeff) + get_stars(p)
					df_column.loc[variable+'_SE', COLUMN_NAME] = '({0:5.4f})'.format(se)
		df_column['Variable'] = df_column.index.values
		df_column = sort_variables(df_column, var2name)
		df_column = df_column.append({'Variable': 'empty'}, ignore_index=True)
		df_column.index = df_column['Variable'].values

		stats = ['aic', 'll', 'N', 'risk']
		for i, stat in enumerate(stats):
			for line in ilines:
				if stat in line:
					s = float(line.split('&')[1])
					if stat in ['N', 'risk']:
						df_column.loc[stat, COLUMN_NAME] = '{0:.0f}'.format(s)
					else:
						df_column.loc[stat, COLUMN_NAME] = '{0:.1f}'.format(s)
		df_data = pd.read_csv('./data/data_{0:s}.csv'.format(EXPERIMENT))
		df_column.loc['Countries', COLUMN_NAME] = '{0:.0f}'.format(df_data['id'].unique().size)
		df_column.loc['Policies', COLUMN_NAME] = '{0:.0f}'.format(df_data['event'].sum())
		df_column['Variable'] = df_column.index.values

		# add column of this model to dataframe, merging on variables
		df_all = df_all.merge(df_column, on=['Variable'], how='outer')

	var2name_plus = deepcopy(var2name)
	variables = [variable for variable in df_all['Variable'].unique() if '_SE' not in variable]
	for variable in variables:
		if variable not in var2name.keys():
			var2name_plus[variable] = variable.replace('_', '.')

	var2name_plus_stats = {**var2name, **stat2name}

	# replace variable names
	index_SE = (df_all['Variable'].str.contains('_SE'))
	df_all.loc[index_SE, 'Variable'] = ''
	df_all.loc[~index_SE, 'Variable'] = df_all.loc[~index_SE, 'Variable'].apply(lambda x: var2name_plus_stats.get(x, x))

	df_all.index = df_all['Variable'].values
	df_all = df_all.drop(columns=['Variable'])

	tablepath = './tables/'
	tablefile = 'table_results_{0:s}.tex'.format(TABLE_ID)
	with pd.option_context("max_colwidth", 1000):
		df_all.to_latex(buf=os.path.join(tablepath, tablefile), index=True, encoding='utf-8', escape=False, column_format='l'+'r'*(df_all.shape[1]), na_rep='')

