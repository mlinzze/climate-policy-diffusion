/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_A01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_A01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_A02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_A02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_A03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_A03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B05.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B05.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B06.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B06.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B07.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B07.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B08.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B08.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_B09.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_B09.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C05.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C05.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_C06.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_C06.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_D01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp industry_share emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_D01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_D02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp g_gdp exports_share imports_share services_share industry_share emission_intensity control_corruption government_effectiveness regulatory_quality rule_of_law reserves_oil reserves_gas reserves_coal exposure_pm25 g_debt government_expenditure belief polity2 welfare spatial_lag i.kyoto i.eu, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_D02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_D03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp g_gdp exports_share imports_share services_share industry_share emission_intensity control_corruption government_effectiveness regulatory_quality rule_of_law reserves_oil reserves_gas reserves_coal exposure_pm25 g_debt spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_D03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_D04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr strata(region) robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_D04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_E01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_E01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_E02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag spatial_lag_sq, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_E02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_E03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag spatial_lag_sq spatial_lag_tr, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_E03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_F01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_F01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_F02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_F02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_F03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_F03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_F04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_F04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_F05.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
estout model1 using ./results/coeffs_F05.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_G01.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag, nohr  robust cluster(id) iterate(500)
estimates store model1
replace log_gdp_pc_ppp = 0
replace emission_intensity = 0
replace government_effectiveness = 0
replace regulatory_quality = 0
replace reserves_oil = 0
replace g_debt = 0
replace government_expenditure = 0
replace polity2 = 0
replace welfare = 0
predict pr, xb
predict se, stdp
outsheet pr se spatial_lag id start stop using ./results/predictions_G01.csv, comma replace
estout model1 using ./results/coeffs_G01.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_G02.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag spatial_lag_sq, nohr  robust cluster(id) iterate(500)
estimates store model1
replace log_gdp_pc_ppp = 0
replace emission_intensity = 0
replace government_effectiveness = 0
replace regulatory_quality = 0
replace reserves_oil = 0
replace g_debt = 0
replace government_expenditure = 0
replace polity2 = 0
replace welfare = 0
predict pr, xb
predict se, stdp
outsheet pr se spatial_lag id start stop using ./results/predictions_G02.csv, comma replace
estout model1 using ./results/coeffs_G02.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_G03.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare spatial_lag spatial_lag_sq spatial_lag_tr, nohr  robust cluster(id) iterate(500)
estimates store model1
replace log_gdp_pc_ppp = 0
replace emission_intensity = 0
replace government_effectiveness = 0
replace regulatory_quality = 0
replace reserves_oil = 0
replace g_debt = 0
replace government_expenditure = 0
replace polity2 = 0
replace welfare = 0
predict pr, xb
predict se, stdp
outsheet pr se spatial_lag id start stop using ./results/predictions_G03.csv, comma replace
estout model1 using ./results/coeffs_G03.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_G04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
mkspline s = spatial_lag, cubic nknots(3) knots(0.05, 0.1, 0.15)
stcox log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare s1 s2, nohr  robust cluster(id) iterate(500)
estimates store model1
replace log_gdp_pc_ppp = 0
replace emission_intensity = 0
replace government_effectiveness = 0
replace regulatory_quality = 0
replace reserves_oil = 0
replace g_debt = 0
replace government_expenditure = 0
replace polity2 = 0
replace welfare = 0
predict pr, xb
predict se, stdp
outsheet pr se spatial_lag id start stop using ./results/predictions_G04.csv, comma replace
estout model1 using ./results/coeffs_G04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
/* ================================================== */
/* https://www.statalist.org/forums/forum/general-stata-discussion/general/1418733-categorical-or-discrete-time-varying-covariates-in-eha-using-streg-and-stcox */
ssc install estout
clear
import delimited ./data/data_G04.csv
stset stop, failure(event==1) id(id)
encode region, gen(region_id)
/* models */
mkspline s = spatial_lag, cubic nknots(3) knots(0.05, 0.1, 0.15)
streg log_gdp_pc_ppp emission_intensity government_effectiveness regulatory_quality reserves_oil g_debt government_expenditure polity2 welfare s1 s2, nohr distribution(exp)  robust cluster(id)
estimates store model2
estout model2 using ./results/coeffs_param_G04.txt, cells(b & se & p) stats(ll r2 p aic bic N risk) varwidth(40) modelwidth(15) delimiter(&) incelldelimiter(|) dmarker(.) style(tab) replace
replace log_gdp_pc_ppp = 0
replace emission_intensity = 0
replace government_effectiveness = 0
replace regulatory_quality = 0
replace reserves_oil = 0
replace g_debt = 0
replace government_expenditure = 0
replace polity2 = 0
replace welfare = 0
predict pr, xb
predict se, stdp
outsheet pr se spatial_lag id start stop using ./results/predictions_G04_exp.csv, comma replace
