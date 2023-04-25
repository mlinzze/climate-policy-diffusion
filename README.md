Overview
--------

The code in this replication package conducts the statistical analysis and produces the results presented in [Linsenmeier et al. 2023](https://mlinsenmeier.com/research/). The package consists of one script for the empirical statistical analysis written in Stata, a program for the Monte Carlo simulations written in C++, and several scripts for visualisation of the results written in Python 3.

Data Availability
----------------------------

All data are publicly available at no cost.

Data on carbon pricing policies:
- Carbon Pricing Dashboard of the World Bank: [https://carbonpricingdashboard.worldbank.org/](https://carbonpricingdashboard.worldbank.org/)
- World Carbon Pricing Database: [https://github.com/g-dolphin/WorldCarbonPricingDatabase](https://github.com/g-dolphin/WorldCarbonPricingDatabase)

Data on country characteristics:
- World Development Indicators of the World Bank (WDI): [https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)
- World Governance Indicators (WGI): [https://info.worldbank.org/governance/wgi/](https://info.worldbank.org/governance/wgi/)
- Greenhouse gas emissions (Minx et al. 2021): [https://doi.org/10.5281/zenodo.5566761](https://doi.org/10.5281/zenodo.5566761)
- Reserves of fossil fuels from the Energy Intelligence Agency (EIA): [https://www.eia.gov/](https://www.eia.gov/)
- Global Debt Database (GDD): [https://www.imf.org/external/datamapper/datasets/GDD](https://www.imf.org/external/datamapper/datasets/GDD)
- Government Finance Statistics (GFS): [https://data.imf.org/?sk=a0867067-d23c-4ebc-ad23-d3b015045405](https://data.imf.org/?sk=a0867067-d23c-4ebc-ad23-d3b015045405)
- Expenditure by Function of Government (COFOG): [https://data.imf.org/?sk=5804c5e1-0502-4672-bdcd-671bcdc565a9](https://data.imf.org/?sk=5804c5e1-0502-4672-bdcd-671bcdc565a9)
- Democracy Index (Polity 5): [https://www.systemicpeace.org/polityproject.html](https://www.systemicpeace.org/polityproject.html)
- Public belief in climate change (Gallup): [https://news.gallup.com/poll/117772/awareness-opinions-global-warming-vary-worldwide.aspx](https://news.gallup.com/poll/117772/awareness-opinions-global-warming-vary-worldwide.aspx)


Computational requirements
---------------------------

### Software Requirements

- Stata 17
  - estout
- Python 3.10.9
  - `numpy` 1.23.4
  - `pandas` 1.5.1
  - `scipy` 1.10.0
  - `statsmodels` 0.13.5
  - `geopandas` 0.12.0
  - `newtorkx` 3.0
  - `matplotlib` 3.6.1
  - `seaborn` 0.12.0
- C++ compiler (for simulations)

The file `requirements.txt` lists these dependencies, please run `pip install -r requirements.txt` as the first step. See [https://pip.readthedocs.io/en/1.1/requirements.html](https://pip.readthedocs.io/en/1.1/requirements.html) for further instructions on using the `requirements.txt` file.

### Memory and Runtime Requirements

Approximate time needed on a standard (2023) desktop machine:
- empirical analysis : 1 hour
- simulations: 7 days (can be shortened by reducing the number of Monte Carlo simulations)

Description of individual scripts
----------------------------

- `stata_all.do`: This script estimates all proportional hazard models and stores the results (estimated coefficients and predicted effects) in the folder `results`.
- `p01_make_latextables.py`: This script uses the estimated coefficients and produces all regression tables shown in the paper and SI.
- `p02_examine_nonlinearities.py`: This script visualises the predicted effects of the non-linear models and then fits an inverse hyperbolic sinus to the model with cubic splines.
- `p03_quantify_emission-reductions.py`: This script uses the results of the Monte Carlo simulations and quantifies the direct and indirect emission reductions from policy diffusion.
- `p04a_visualise_emission_reductions.py`: This script visualises the direct and indirect emission reductions.
- `p04b_visualise_centrality.py`: This script calculates network centrality measures for all countries, regresses indirect emission reductions on those measures, and visualises the statistical associations with scatter plots.
- `p04c_visualise_coverage.py`: This script visualises the results of the Monte Carlo simulations including the sensitivity analysis in terms of the share of countries/global emissions with a carbon pricing policy for scenarios with and without policy diffusion.
- `p04c_visualise_effectivenes.py`: This script visualises the indirect emission reductions for different assumptions about the effectiveness of carbon pricing policies.

### License for Code

The code in this repository is licensed under a CC-BY-NC license.

Instructions to Replicators
---------------------------

- Run all scripts in the order indicated by the file names (i.e. `p01`, `p02`, `p03`, ...). This can also be achieved with the Makefile in the repository (`make clean; make all`).
- Some of the scripts store intermediate results in the folder `results`.
- Once all scripts have finished, all tables and figures can be found in the respective folders `tables` and `figures`.
- For the simulations, see the separate Makefile in the folder `simulations`.
