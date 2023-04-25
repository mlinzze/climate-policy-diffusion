export CFLAGS=" -g -O2 -lm -ldl -Wall -Wpointer-arith -finline-functions -ffast-math -funroll-all-loops"
export LD_LIBRARY_PATH=/home/manuel/anaconda3/lib

install:
	make clean
	c++ -c functions.c -lm -ldl -o functions.o
	c++ montecarlo.c -I${NETCDF_HOME}/include -I./ -L${NETCDF_HOME}/lib -L./ -lm -ldl -o montecarlo.x functions.o
	c++ montecarlo_sensitivity.c -I${NETCDF_HOME}/include -I./ -L${NETCDF_HOME}/lib -L./ -lm -ldl -o montecarlo_sensitivity.x functions.o
	c++ montecarlo_sensitivity100.c -I${NETCDF_HOME}/include -I./ -L${NETCDF_HOME}/lib -L./ -lm -ldl -o montecarlo_sensitivity100.x functions.o

set1:
	./montecarlo.x mix nonlinear future current counterfactual
	./montecarlo.x mix nonlinear future current treatment

set2:
	./montecarlo.x grv nonlinear future current counterfactual
	./montecarlo.x grv nonlinear future current treatment
	./montecarlo.x igo nonlinear future current counterfactual
	./montecarlo.x igo nonlinear future current treatment

set3:
	./montecarlo_sensitivity.x mix nonlinear future current diffusion
	./montecarlo_sensitivity.x mix nonlinear future current nodiffusion

set4:
	./montecarlo_sensitivity100.x mix nonlinear future100 current diffusion
	./montecarlo_sensitivity100.x mix nonlinear future100 current nodiffusion

all:
	make install
	make set1
	make set2
	make set3
	make set4

clean:
	rm -f functions.o