#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#define	TRUE 1
#define	FALSE 0

int getfield(char* line, int num, char **entry);

int readP(const char *filename, int ntimes, int ncountries, int first_year, double **P);

int readCountryNames(const char *filename, int ncountries, char **countrynames);

int readX(const char *filename, int ntimes, int ncountries, int nvariables, int first_year, double ***X);

int readW(const char *filename, int ntimes, int ncountries, int first_year, double ***W);

int writePr(const char *filename, int ntimes, int ncountries, int precision, char **countrynames, int first_year, double **Pr);

int weibull(double p, double x, double intercept, double *result);

int exponential(double intercept, double *result);

int hazardnonlinear(int size, double *a, double *b);

int matrixplusmatrix(int nrows, int ncolumns, double **a, double **b, double **c);

int vectorplusvector(int size, double *a, double *b, double *c);

int vectorplusconstant(int size, double *a, double b);

int vectortimesvector(int size, double *a, double *b, double *c);

int scalarvectorproduct(int size, double a, double *b, double *c);

int scalarvectorproduct2(int size, double a, double *b);

int matrixproduct(int nrows, int ncolumns_a, int ncolumns_b, double **a, double **b, double **m);

int matrixvectorproduct(int nrows, int ncolumns, double **m, double *a, double *b);

int normalise_array(int nrows, int ncolumns, double **a, double *b);

int normalise_matrix(int nrows, int ncolumns, double a, double **b);

int fill_zeros_2d(int nrows, int ncolumns, double **a);

int fill_zeros_array(int size, double *a);

int fill_random_2d(int nrows, int ncolumns, double **a);

int fill_random_array(int size, double *a);

int fill_diagonal_2d(int nrows, int ncolumns, double **a);

int copy_values_2d(int nrows, int ncolumns, double **a, double **b);

int get_precision(int nmontecarlo, int *precision);

int print_array(int nrows, char **labels, double *a);

int print_matrix(int nrows, int ncols, char **labels_rows, char **labels_cols, double **a);

#endif /* FUNCTIONS_H */
