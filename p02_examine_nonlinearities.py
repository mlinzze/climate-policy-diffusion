#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy

import scipy.stats
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import statsmodels
import statsmodels.api as sm

## ============================================================
## visualise predictions for non-linear terms
## ============================================================

df_lag = pd.read_csv('./data/spatial_lags.csv')
df_lag = df_lag.loc[df_lag['year'] >= 1988, :].rename(columns={\
			'price_first_proximity_gdp_igo': 'spatial_lag'})
m = df_lag['spatial_lag'].mean()
sd = df_lag['spatial_lag'].std()
m = 0.
sd = 1.

fig, ax = plt.subplots(figsize=(5,4))

experiment_lin = 'G01' # linear
df = pd.read_csv('./results/predictions_{0:s}.csv'.format(experiment_lin))
df = df.sort_values(by=['spatial_lag'], ascending=True)
df['spatial_lag'] = df['spatial_lag']*sd + m
df['pr'] = df['pr'] - df['pr'].mean()
ax.plot(df['spatial_lag'], df['pr'], 'ko', markersize=1., label='linear')

experiment_sq = 'G02' # squared
df = pd.read_csv('./results/predictions_{0:s}.csv'.format(experiment_sq))
df = df.sort_values(by=['spatial_lag'], ascending=True)
df['spatial_lag'] = df['spatial_lag']*sd + m
df['pr'] = df['pr'] - df['pr'].mean()
ax.plot(df['spatial_lag'], df['pr'], 'bo', markersize=1., label='quadratic')

experiment_cub = 'G03' # cubic
df = pd.read_csv('./results/predictions_{0:s}.csv'.format(experiment_cub))
df = df.sort_values(by=['spatial_lag'], ascending=True)
df['spatial_lag'] = df['spatial_lag']*sd + m
df['pr'] = df['pr'] - df['pr'].mean()
ax.plot(df['spatial_lag'], df['pr'], 'ro', markersize=1., label='cubic')

experiment_spl = 'G04' # cubic splines
df = pd.read_csv('./results/predictions_{0:s}.csv'.format(experiment_spl))
df = df.sort_values(by=['spatial_lag'], ascending=True)
df['spatial_lag'] = df['spatial_lag']*sd + m
df['pr'] = df['pr'] - df['pr'].mean()
ax.plot(df['spatial_lag'], df['pr'], 'go', markersize=1., label='cubic splines')

xticks = np.arange(0., 0.45, 0.05)
ax.set_xticks(xticks)
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.025))
bins = np.arange(0., 0.45, 0.025)

ax2 = ax.twinx()

## bins
y = df_lag['spatial_lag']
ax2.hist(y, bins=bins, color='grey')
ymax = y.groupby(pd.cut(y, bins)).count().max()
ax2.set_ylim(-ymax*0.7, ymax*10.)
ax2.set_yticks([])

ax.set_ylabel('Linear prediction')
ax.set_xlabel('Spatial lag')
ax.legend(loc='lower right')
sns.despine(ax=ax, offset=1., right=True, top=True)
sns.despine(ax=ax2, offset=1., left=True, right=True, top=True)
fig.savefig('./figures/predictions_nonlinear.pdf', bbox_inches='tight')

## ============================================================
## fit simpler function instead of splines
## ============================================================

import scipy.optimize

experiment = "G04"

# spline
df = pd.read_csv('./results/predictions_{0:s}_exp.csv'.format(experiment))
df = df.sort_values(by=['spatial_lag'], ascending=True)
x = df['spatial_lag'].values
y = df['pr'].values
ymean = np.mean(y)

xfit = np.linspace(np.min(x), 0.4, 10000)
yfit = np.interp(xfit, x, y)
xextra = np.linspace(0.4, 1., 2)
res = scipy.stats.linregress(x=xfit[xfit>0.3], y=yfit[xfit>0.3])
yextra = res.intercept + res.slope * xextra
xi = np.hstack((xfit, xextra))
yi = np.hstack((yfit, yextra))

def func(params, x=x):
	return params[0] + params[1] * np.arcsinh(params[2] + x * params[3])
def cost(params, x=xi, y=yi):
	return np.mean((y - func(params, x))**2.)
res = scipy.optimize.least_squares(cost,
									x0 = [-10, 1., 0., 10.],
									bounds=([-20., -10., -10., 0.], [20., 10., 10., 100.]),
									verbose=1, max_nfev=10000.)
formula = '{0: 5.4f} + {1: 5.4f} * PLACEHOLDER({2: 5.4f} + {3: 5.4f} * x)'.format(\
			res.x[0], res.x[1], res.x[2], res.x[3]).replace('PLACEHOLDER', 'sinh$^{-1}$')

xopt = np.linspace(0., 1., 1000)
yopt = func(params=res.x, x=xopt)

## ============================================================

fig, ax = plt.subplots(figsize=(5,4))
ax.plot(xfit, yfit, 'k-', markersize=0.5, label='empirical estimate')
ax.plot(xextra, yextra, 'k--', markersize=0.5)
ax.plot(xopt, yopt, 'm-', markersize=0.5, label=formula)
ax.set_ylabel('Linear prediction')
ax.set_xlabel('Spatial lag')
ax.legend(loc='upper left')
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig('./figures/predictions_nonlinear_fitted.pdf', bbox_inches='tight')

