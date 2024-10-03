#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include <cmath>
#include <iostream>
#include <random>

#define j 64 //maximum number of threads (aveliable from AUTh's cluster)

double montecarlo (int points)
{
   
	
	long long int i;
    long long int sum=0;
	double x,y;
	int r=1;

		#pragma omp parallel private(i,x,y) reduction(+:sum) 
       {                  
        
        unsigned int seed=omp_get_thread_num()+(unsigned int)time(NULL); // Different seed for each thread
        std::mt19937 generator(seed); // Generator for the random numbers berween 0 and 1
        std::uniform_real_distribution<double> distribution(0.0, 1.0);
							
		
        #pragma omp for schedule(static)
        for(i=0;i< points;i++)
		{  
			x=distribution(generator)*r;
            y=distribution(generator)*r;
			if ((pow(x,2)+pow(y,2))<=pow(r,2)) sum+=1;


        }

	   
            
	   }

return ((double)sum/points)*4.0;; //pi estimation

}

int main ()
{
	long long int N; //Number of points
	std::cin>>N;

	omp_set_dynamic(0); 
	omp_set_num_threads(j); //set number of threads 
	
	
	double startt=omp_get_wtime();
	double p=montecarlo(N);
	double endt=omp_get_wtime();

	
	std::cout<<"With "<<N<<" points pi is estimated as "<<p<<std::endl;
	double tottime=endt-startt;
	//std::cout<<"Execution Time: " <<tottime.count() <<std::endl;
	std::cout.flush();
	

	
	return 0;
}
