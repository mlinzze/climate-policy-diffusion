#include  <stdio.h>
#include  <math.h>
#include  <string.h>
#include "functions.h"

int main(int argc, char *argv[])
{

	int DEBUG = 0;
	int ncountries = 188;
	int nvariables = 9;

	const char* metric = argv[1];
	const char* model = argv[2];
	const char* time_period = argv[3];
	const char* policies = argv[4];
	const char* scenario = argv[5];

	printf("## ======================================== ##\n");
	printf("*** Metric: %s \n", metric);
	printf("*** Model: %s \n", model);
	printf("*** Time period: %s \n", time_period);
	printf("*** Policies: %s \n", policies);
	printf("*** Scenario: %s \n", scenario);

	int first_year;
	int ntimes;
	int nmontecarlo;
	int treatment;
	int ntreated;

	int N_BASELINE = 7;
	double baseline_factor[N_BASELINE] = { 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2. };
	int N_DIFFUSION = 7;
	double diffusion_factor[N_DIFFUSION] = { 0.5, 0.75, 1., 1.25, 1.5, 1.75, 2. };

	if (!strcmp(time_period, "past")) {
		printf(" ERROR: Not implemented ");
		return(1);
	}
	if (!strcmp(time_period, "future")) {
		first_year = 2021;
		ntimes = 30;
	}
	if (!strcmp(scenario, "diffusion")) {
		nmontecarlo = 10000;
		treatment = 0;
		ntreated = 1;
	}
	if (!strcmp(scenario, "nodiffusion")) {
		nmontecarlo = 10000;
		treatment = 0;
		ntreated = 1;
	}

	int precision;
	if(nmontecarlo % 10 == 0)
	{
		get_precision(nmontecarlo, &precision);
	} else {
		precision = 4;
	}

	char filenameW_temp[120];
	sprintf(filenameW_temp, "./data_W_%s_%s.csv", metric, time_period);
	const char* filenameW = &filenameW_temp[0];

	char filenameX_temp[120];
	sprintf(filenameX_temp, "./data_X_%s.csv", time_period);
	const char* filenameX = &filenameX_temp[0];

	char filenameP_temp[120];
	sprintf(filenameP_temp, "./data_P_%s.csv", time_period);
	const char* filenameP = &filenameP_temp[0];

	const char filenameCountries[120] = "./countries.csv";

	char output_directory_temp[120];
	sprintf(output_directory_temp, "./results_%s_%s_%s_%s", metric, model, time_period, policies);
	const char* output_directory = &output_directory_temp[0];

	// allocate regression coefficients of covariates
	double beta_X[nvariables];
	double beta_W;

	// exponential parameter
	double constant;

	// assign values of coefficients
	if (!strcmp(model, "linear")) {
		printf(" ERROR: Not implemented ");
		return(1);
	}
	if (!strcmp(model, "nonlinear")) {
		beta_X[0] = 0.34993 ; // emission_intensity
		beta_X[1] = 0.11895 ; // g_debt
		beta_X[2] = -0.33287 ; // government_effectiveness
		beta_X[3] = 0.13532 ; // government_expenditure
		beta_X[4] = 0.63651 ; // log_gdp_pc_ppp
		beta_X[5] = 0.35472 ; // polity2
		beta_X[6] = 1.32403 ; // regulatory_quality
		beta_X[7] = 0.01475 ; // reserves_oil
		beta_X[8] = 0.30903 ; // welfare
		constant = -7.23811 ; // intercept included
	}

	if (!strcmp(time_period, "past")) {
		if (!strcmp(policies, "current")) {
			printf(" ERROR: Not implemented ");
			return(1);
		}
	}

	char *countrynames[ncountries];
	int t, c;

	// allocate X [ntimes, ncountries, nvariables]
	double ***X = (double ***)malloc(sizeof(double **) * ntimes);
	for (t = 0; t < ntimes; t++)
	{
		X[t] = (double **)malloc(sizeof(double *) * ncountries); 
		for (c = 0; c < ncountries; c++)
		{
			X[t][c] = (double *)malloc(sizeof(double) * nvariables); 
		}
	}

	// allocate Xt [ncountries, nvariables] # covariates
	double **Xt = (double **)malloc(sizeof(double *) * ncountries);
	for (c = 0; c < ncountries; c++)
		Xt[c] = (double *)malloc(sizeof(double) * nvariables); 

	// allocate W [ntimes, ncountries, countries]
	double ***W = (double ***)malloc(sizeof(double **) * ntimes);
	for (t = 0; t < ntimes; t++)
	{
		W[t] = (double **)malloc(sizeof(double *) * ncountries); 
		for (c = 0; c < ncountries; c++)
		{
			W[t][c] = (double *)malloc(sizeof(double) * ncountries); 
		}
	}

	// allocate Wt [ncountries, ncountries] # covariates
	double **Wt = (double **)malloc(sizeof(double *) * ncountries);
	for (c = 0; c < ncountries; c++)
		Wt[c] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Wt [ncountries, 1] # spatial lag
	double Wtc[ncountries];

	// allocate P [ntimes, ncountries] # actual adoption
	double **P = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		P[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pn [ntimes, ncountries] # adoption in specific run
	double **Pn = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pn[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pr [ntimes, ncountries] # store the results here
	double **Pr = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pr[t] = (double *)malloc(sizeof(double) * ncountries); 

	// allocate Pf [ntimes, ncountries] # first adoption in that simulation
	double **Pf = (double **)malloc(sizeof(double *) * ntimes);
	for (t = 0; t < ntimes; t++)
		Pf[t] = (double *)malloc(sizeof(double) * ncountries); 

	// treatment
	int unit_treated;
	int time_treated = 0;

	// arrays for the hazard rate
	double hazard_X[ncountries];
	double hazard_W[ncountries];
	double hazard_baseline[ncountries];
	double hazard[ncountries];

	double draw; // for random number

	// ========================= assign values =========================

	readCountryNames(filenameCountries, ncountries, countrynames);

	readX(filenameX, ntimes, ncountries, nvariables, first_year, X);

	readW(filenameW, ntimes, ncountries, first_year, W);

	readP(filenameP, ntimes, ncountries, first_year, P);

	// only for testing and debugging
	int unit_debug = 94;
	if (DEBUG == 1)
	{
		printf("Debug unit: %s\n", countrynames[unit_debug]);
		printf("Debug unit policy in last year: %f\n", P[ntimes-1][unit_debug]);
		//printf("value of X: %f\n", X[0][0][0]);
		//printf("weight from W: %f\n", W[1][1]);
	}
	//fill_random_2d(ntimes, ncountries, P);
	//fill_random_2d(ncountries, ncountries, W);
	//fill_random_array(ncountries, Wtc);
	//fill_zeros_2d(ntimes, ncountries, P);
	//fill_zeros_2d(ntimes, ncountries, P);
	fill_zeros_2d(ntimes, ncountries, Pr);

	int n;
	double bf, df;
	int i_baseline, i_diffusion;

	for(i_baseline = 0; i_baseline < N_BASELINE; i_baseline++)
	{
		bf = baseline_factor[i_baseline];

		if (DEBUG == 1)
		{
			printf("Baseline factor: %f\n", bf);
		}	

		for(i_diffusion = 0; i_diffusion < N_DIFFUSION; i_diffusion++)
		{
			df = diffusion_factor[i_diffusion];

			if (DEBUG == 1)
			{
				printf("Diffusion factor: %f\n", df);
			}	

			fill_zeros_2d(ntimes, ncountries, Pr);

			for(unit_treated = 0; unit_treated < ntreated; unit_treated++)
			{
				if (!strcmp(scenario, "treatment")) {
					printf("Treatment unit: %s\n", countrynames[unit_treated]);
				}

				fill_zeros_2d(ntimes, ncountries, Pr);

				for (n = 0; n < nmontecarlo; n++)
					{
					if (DEBUG == 1)
					{
						printf("Monte Carlo: %i\n", n);
					}

					if (!strcmp(policies, "none")) {
						fill_zeros_2d(ntimes, ncountries, Pn);
					}
					if (!strcmp(policies, "current")) {
						copy_values_2d(ntimes, ncountries, P, Pn);
					}

					Pn[time_treated][unit_treated] = treatment;

					for (t = time_treated+1; t < ntimes; t++)
						{
						if (DEBUG == 1)
						{
							printf("## =========== ##\n");
							printf("Country : %s\n", countrynames[unit_debug]);
							printf("Year : %i\n", t);
						}
						copy_values_2d(ncountries, ncountries, W[t-1], Wt);
						//print_matrix(ncountries, ncountries, countrynames, countrynames, Wt);
						matrixvectorproduct(ncountries, ncountries, Wt, Pn[t-1], Wtc);
						normalise_array(ncountries, ncountries, Wt, Wtc);

						if (DEBUG == 1)
						{
							printf("W: %f\n", Wtc[unit_debug]);
						}

						if (!strcmp(scenario, "nodiffusion")) {
							scalarvectorproduct2(ncountries, 0., Wtc);
							vectorplusconstant(ncountries, Wtc, 0.055544); // minimum in 2022
						}

						if (!strcmp(scenario, "diffusion")) {
							scalarvectorproduct2(ncountries, df, Wtc);
						}

						if (DEBUG == 1)
						{
							printf("W (sensitivity): %f\n", Wtc[unit_debug]);
						}

						copy_values_2d(ncountries, nvariables, X[t-1], Xt);
						matrixvectorproduct(ncountries, nvariables, Xt, beta_X, hazard_X);

						if (!strcmp(model, "linear")) {
							scalarvectorproduct(ncountries, beta_W, Wtc, hazard_W);
						}
						if (!strcmp(model, "nonlinear")) {
							hazardnonlinear(ncountries, Wtc, hazard_W);
						}
						
						if (DEBUG == 1)
						{
							printf("hazard X: %f\n", hazard_X[unit_debug]);
							printf("hazard W: %f\n", hazard_W[unit_debug]);
						}

						if (DEBUG == 1)
						{
							printf("hazard W (sensitivity): %f\n", hazard_W[unit_debug]);
						}

						vectorplusvector(ncountries, hazard_X, hazard_W, hazard);
						for(c=0; c < ncountries; c++)
							hazard[c] = exp(hazard[c]);
						if (DEBUG == 1)
						{
							printf("exp hazard total: %f\n", hazard[unit_debug]);
						}
						fill_zeros_array(ncountries, hazard_baseline);
						
						for(c=0; c < ncountries; c++)
						{	
							hazard_baseline[c] = exp(constant);
						}
						
						if (DEBUG == 1)
						{
							printf("hazard baseline: %f\n", hazard_baseline[unit_debug]);
						}

						scalarvectorproduct2(ncountries, bf, hazard_baseline);

						if (DEBUG == 1)
						{
							printf("hazard baseline (sensitivity): %f\n", hazard_baseline[unit_debug]);
						}

						vectortimesvector(ncountries, hazard, hazard_baseline, hazard);
						if (DEBUG == 1)
						{
							printf("hazard total * baseline: %f\n", hazard[unit_debug]);
						}

						for(c=0; c < ncountries; c++)
						{
							if (Pn[t-1][c] == 1)
							{
								hazard[c] = 1;
							}
							if (hazard[c] > 1)
							{
								hazard[c] = 1;
							}
							if (hazard[c] < 0)
							{
								hazard[c] = 0;
							}
						}
						if (DEBUG == 1)
						{
							printf("hazard (effective): %f\n", hazard[unit_debug]);
						}
						for(c=0; c < ncountries; c++)
						{
							draw = ((double) rand() / (double) RAND_MAX);
							Pn[t][c] = 0;
							if (DEBUG == 1)
							{
								if (c == unit_debug)
									printf("draw: %f\n", draw);
							}
							if (draw <= hazard[c])
							{
								Pn[t][c] = 1;
							}
						}

						Pn[t][unit_treated] = treatment;
						if (DEBUG == 1)
						{
							printf("policy: %f\n", Pn[t][unit_debug]);
						}
					}
					
					fill_zeros_2d(ntimes, ncountries, Pf);

					for (c = 0; c < ncountries; c++)
					{
						for(t = 0; t < ntimes; t++)
						{
							if (Pn[t][c] == 1.)
							{
								Pf[t][c] = 1.;
								break;
							}
						}
					}

					matrixplusmatrix(ntimes, ncountries, Pr, Pf, Pr);			
				}
				
				double nmontecarlo_double = (double) nmontecarlo;
				normalise_matrix(ntimes, ncountries, nmontecarlo_double, Pr);

				char unit_name[3];
				int diffusion;
				if (!strcmp(scenario, "diffusion")) {
					sprintf(unit_name, "%s", "ANY");
					diffusion = 1;
				}
				if (!strcmp(scenario, "nodiffusion")) {
					sprintf(unit_name, "%s", "ANY");
					diffusion = 0;
				}
				char string_filename[120];
				sprintf(string_filename,  "%s/result_%s_%i_b%i_d%i.csv", output_directory, unit_name, diffusion, i_baseline, i_diffusion);
				printf("Writing to file: %s\n", string_filename);
				writePr(string_filename, ntimes, ncountries, precision, countrynames, first_year, Pr);
			} // end normal program
		}
	} // end sensitivity
	return(0);
}
