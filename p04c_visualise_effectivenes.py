#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from copy import deepcopy

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================

IPATH = './simulations/results_mix_nonlinear_future_current/'

## ============================

sample_price = pd.read_csv('./simulations/data_P_future.csv', names=['year', 'iso', 'price']).\
				groupby('iso')['price'].max()
sample_price = sample_price[sample_price == 1].index.values

## ============================

fig, ax = plt.subplots(figsize=(6,4))
ax2 = ax.twinx()
x = []
y1 = []
y2 = []
y3 = []
for i, EFFECT_SIZE in enumerate([0.005, 0.01, 0.02, 0.05, 0.1]):
	df = pd.read_csv(os.path.join(IPATH, 'emission_reductions_effectsize_{0:4.3f}.csv'.format(EFFECT_SIZE)))
	df = df.loc[~df['iso'].isin(sample_price), :]
	x.append(EFFECT_SIZE)
	y1.append(df['direct'].median())
	y2.append(df['indirect'].median())
	y3.append((df['indirect'] > df['direct']).sum()/ df['indirect'].count()*100.)
	print(EFFECT_SIZE, y3[-1])
ax.plot(x, y1, 'b--o', markersize=5, label='Direct emission red. (median)')
ax.plot(x, y2, 'r--s', markersize=5, label='Indirect emission red. (median)')
ax2.plot(x, y3, 'k:o', markersize=5, label='Indirect > direct')
ax.set_xlabel('Effectiveness of policy')
ax.set_ylabel('Emission reductions (Gt)')
ax2.set_ylabel('Countries with indirect > direct (%)')
ax.set_ylim(0., 0.7)
ax2.set_ylim(50, 90.)
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
sns.despine(ax=ax, offset=1., right=False, top=True)
sns.despine(ax=ax2, offset=1., left=False, top=True)
fig.savefig('./figures/scatter_effectiveness.pdf', bbox_inches='tight', transparent=True)
fig.savefig('./figures/scatter_effectiveness.png', bbox_inches='tight', transparent=True, dpi=300)
