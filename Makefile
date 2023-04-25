
stata:
	stata -b do ./stata_all.do, nostop

statistics:
	python3 ./p01_make_latextables.py
	python3 ./p02_examine_nonlinearities.py
	python3 ./p03_quantify_emission-reductions.py

visualisation:
	python3 ./p04a_visualise_emission_reductions.py
	python3 ./p04b_visualise_centrality.py
	python3 ./p04c_visualise_coverage.py
	python3 ./p04c_visualise_effectivenes.py

all:
	make stata
	make statistics
	make visualisation