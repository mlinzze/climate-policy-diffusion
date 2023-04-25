#include  <stdio.h>
#include  <stdlib.h>
#include  <string.h>
#include  <math.h>
#include "functions.h"

int readCountryNames(const char *filename, int ncountries, char **countrynames)
{
	char line[60];
	char *country;

	FILE* stream = fopen(filename, "r");
	printf("opening now to read country names: '%s'\n", filename);

	int icountry = 0;
	char* tmp;

	while (icountry < ncountries)
	{
		if (fgets(line, 1024, stream))
		{
			tmp = strdup(line);
			tmp[strcspn(tmp, "\r\n")] = 0;
			getfield(tmp, 0, &country);
			char *countrystring = strdup(country);
			free(tmp);
			//printf("country: '%s'\n", countrystring);
			countrynames[icountry] = countrystring;
			icountry += 1;
		}
		else
			break;
	}
	return(0);
}

int readX(const char *filename, int ntimes, int ncountries, int nvariables, int first_year, double ***X)
{
	char line[60];
	char *year;
	char *country;
	char *variable;
	char *value;

	int iyear, icountry, ivariable;

	FILE* stream = fopen(filename, "r");
	printf("opening now to read data X: '%s'\n", filename);

	int iline = 0;
	char* tmp;

	while (fgets(line, 1024, stream))
	{
		tmp = strdup(line);
		getfield(tmp, 0, &year);
		tmp = strdup(line);
		getfield(tmp, 1, &country);
		tmp = strdup(line);
		getfield(tmp, 2, &variable);
		tmp = strdup(line);
		getfield(tmp, 3, &value);

		//printf("'%s'\n", line);
		//printf("'%s %s %s'\n", year, country, variable);

		iyear = atoi(year) - first_year;
		icountry = (iline / nvariables) % ncountries;
		ivariable = iline % nvariables;

		//printf("'%i %i %i'\n", iyear, icountry, ivariable);

		X[iyear][icountry][ivariable] = atof(value);
		free(tmp);

		iline += 1;
	}
	return(0);
}


int readP(const char *filename, int ntimes, int ncountries, int first_year, double **P)
{
	char line[60];
	char *year;
	char *country;
	char *value;

	int iyear, icountry;

	FILE* stream = fopen(filename, "r");
	printf("opening now to read data P: '%s'\n", filename);

	int iline = 0;
	char* tmp;

	while (fgets(line, 1024, stream))
	{
		tmp = strdup(line);
		getfield(tmp, 0, &year);
		tmp = strdup(line);
		getfield(tmp, 1, &country);
		tmp = strdup(line);
		getfield(tmp, 2, &value);

		//printf("'%s'\n", line);
		//printf("'%s %s %s'\n", year, country, variable);

		iyear = atoi(year) - first_year;
		icountry = iline % ncountries;

		//printf("'%i %i %s %s'\n", iyear, icountry, country, value);

		P[iyear][icountry] = atof(value);
		free(tmp);

		iline += 1;
	}
	return(0);
}

int readW(const char *filename, int ntimes, int ncountries, int first_year, double ***W)
{
	char line[60];

	FILE* stream = fopen(filename, "r");
	printf("opening now to read data W: '%s'\n", filename);

	int iline = 0;
	int iyear;
	int icountry1;
	int icountry2;
	int markup = 0; // needed because of missing diagonal elements in file

	char *tmp;
	char *year;
	char *value;
	char *country1;
	char *country2;

	while (fgets(line, 1024, stream))
	{

		icountry1 = (iline / (ncountries - 1)) % ncountries;
		icountry2 = iline % (ncountries - 1);

		if (icountry2 >= icountry1) {
			markup = 1;
		} else {
			markup = 0;
		}

		tmp = strdup(line);
		getfield(tmp, 0, &year);
		tmp = strdup(line);
		getfield(tmp, 1, &country1);
		tmp = strdup(line);
		getfield(tmp, 2, &country2);
		tmp = strdup(line);
		getfield(tmp, 3, &value);

		iyear = atoi(year) - first_year;
		W[iyear][icountry1][icountry2 + markup] = atof(value);

		//printf("## === ##\n");
		//printf("'%s'", line);
		//printf("%i %i %i\n", iyear, icountry1, icountry2 + markup);

		free(tmp);
		iline += 1;

	}
	for (iyear=0; iyear < ntimes; iyear++) {
		for (icountry1=0; icountry1 < ncountries; icountry1++) {
			W[iyear][icountry1][icountry1] = 0.;
		}
	}

	return(0);
}

int getfield(char *line, int num, char **entry)
{
	char *token;
	int i = 0;
	token = strtok(line, ",");
	while(token != NULL) {
		while (i < num)
		{
			token = strtok(NULL, ",");
			i += 1;
			//printf(" %i\n", i);
		}
		//printf(" %s\n", token);
		*entry = token;
		break;
	}
	return(0);
}

int writePr(const char *filename, int ntimes, int ncountries, int precision, char **countrynames, int first_year, double **Pr)
{

	FILE* stream = fopen(filename, "w");

	int t;
	int c;
	
	for (t = 0; t < ntimes; t++)
	{
		for (c = 0; c < ncountries; c++)
		{	
			//printf("%s\n", countrynames[c]);
			if(precision == 1)
				fprintf(stream, "%i,%s,%2.1f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 2)
				fprintf(stream, "%i,%s,%3.2f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 3)
				fprintf(stream, "%i,%s,%4.3f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 4)
				fprintf(stream, "%i,%s,%5.4f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 5)
				fprintf(stream, "%i,%s,%6.5f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 6)
				fprintf(stream, "%i,%s,%7.6f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 7)
				fprintf(stream, "%i,%s,%8.7f\n", t+first_year, countrynames[c], Pr[t][c]);
			if(precision == 8)
				fprintf(stream, "%i,%s,%9.8f\n", t+first_year, countrynames[c], Pr[t][c]);
		}
	}
	fclose(stream);
	return(0);
}

int weibull(double p, double x, double intercept, double *result)
{
	*result = p * (pow(x, p - 1)) * exp(intercept);
	return(0);
}

int exponential(double intercept, double *result)
{
	*result = exp(intercept);
	return(0);
}

int hazardnonlinear(int size, double *a, double *b)
{
	int i;
	for(i=0; i < size; i++)
	{    
		b[i] = + 1.0253 * asinh(-1.2345 + 33.2971 * a[i]); //
	}
	return(0);
}

int fill_zeros_2d(int nrows, int ncolumns, double **a)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns; j++)    
		{    
			a[i][j]=0.; 
		}  
	}
	return(0);
}

int fill_zeros_array(int size, double *a)
{
	int i;
	for(i=0; i < size; i++)
	{    
		a[i]=0.; 
	}
	return(0);
}

int fill_random_2d(int nrows, int ncolumns, double **a)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns; j++)    
		{    
			a[i][j]=rand(); 
		}  
	}
	return(0);
}

int fill_random_array(int size, double *a)
{
	int i;
	for(i=0; i < size; i++)
	{    
		a[i]=rand(); 
	}
	return(0);
}

int fill_diagonal_2d(int nrows, int ncolumns, double **a)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns; j++)    
		{    
			a[i][j]=0.;
			if(i == j)
			{
				a[i][j]=1.;
			}
		}  
	}
	return(0);
}

int matrixplusmatrix(int nrows, int ncolumns, double **a, double **b, double **c)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns; j++)    
		{    
			c[i][j]=a[i][j]+b[i][j]; 
		}
	}
	return(0);
}

int vectorplusvector(int size, double *a, double *b, double *c)
{
	int i;
	for(i=0; i < size; i++)
	{    
		c[i]=b[i]+a[i]; 
	}
	return(0);
}

int vectorplusconstant(int size, double *a, double b)
{
	int i;
	for(i=0; i < size; i++)
	{    
		a[i]=a[i]+b; 
	}
	return(0);
}

int vectortimesvector(int size, double *a, double *b, double *c)
{
	int i;
	for(i=0; i < size; i++)
	{    
		c[i]=b[i]*a[i]; 
	}
	return(0);
}

int scalarvectorproduct(int size, double a, double *b, double *c)
{
	int i;
	for(i=0; i < size; i++)
	{    
		c[i]=b[i]*a; 
	}
	return(0);
}

int scalarvectorproduct2(int size, double a, double *b)
{
	int i;
	for(i=0; i < size; i++)
	{    
		b[i]=b[i]*a; 
	}
	return(0);
}

int matrixproduct(int nrows, int ncolumns_a, int ncolumns_b, double **a, double **b, double **m)
{
	int i, j, k;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns_b; j++)    
		{    
		m[i][j]=0.;    
		for(k=0; k < ncolumns_a; k++)    
			{    
			m[i][j] += a[i][k] * b[k][j];    
			}
		}
	}
   return(0);
}

int matrixvectorproduct(int nrows, int ncolumns, double **m, double *a, double *b)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		b[i]=0.;    
		for(j=0; j < ncolumns; j++)    
		{    
			b[i] += m[i][j] * a[j];    
		}
	}
   return(0);
}

int normalise_array(int nrows, int ncolumns, double **a, double *b) // divide each entry in b by corresponding column sum of matrix a
{
	int i, j;
	double weight;
	for(i=0; i < nrows; i++)
	{
		weight = 0.;
		for(j=0; j < ncolumns; j++)    
		{    
			weight += a[i][j];
		}
		b[i] = b[i] / weight;
		if (weight == 0)
		{
			b[i] = 0.;
		}
	}
	return(0);
}

int normalise_matrix(int nrows, int ncolumns, double a, double **b)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{
		for(j=0; j < ncolumns; j++)    
		{    
			b[i][j] = b[i][j]/a;
		}
	}
	return(0);
}

int copy_values_2d(int nrows, int ncolumns, double **a, double **b)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{    
		for(j=0; j < ncolumns; j++)    
		{    
			//b[i][j] = a[i][j];
			memcpy(&b[i][j], &a[i][j], sizeof(double));
		}  
	}
	return(0);
}

int get_precision(int nmontecarlo, int *precision)
{
	*precision = 4;
	if(nmontecarlo == 10)
		*precision = 1;
	if(nmontecarlo == 100)
		*precision = 2;
	if(nmontecarlo == 1000)
		*precision = 3;
	if(nmontecarlo == 10000)
		*precision = 4;
	if(nmontecarlo == 100000)
		*precision = 5;
	if(nmontecarlo == 1000000)
		*precision = 6;
	return(0);
}

int print_array(int nrows, char **labels, double *a)
{
	int i;
	for(i=0; i < nrows; i++)
	{
		printf("%s %f\n", labels[i], a[i]);

	}
	return(0);
}

int print_matrix(int nrows, int ncols, char **labels_rows, char **labels_cols, double **a)
{
	int i, j;
	for(i=0; i < nrows; i++)
	{
		for(j=0; j < ncols; j++)
		{
			printf("%s %s %f\n", labels_rows[i], labels_cols[j], a[i][j]);
		}
	}
	return(0);
}