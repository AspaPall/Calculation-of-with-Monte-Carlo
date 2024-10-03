import subprocess
import os
import re
import numpy as np
import matplotlib.pyplot as plt

numthreads=[[1],[2],[4],[8],[16],[32],[64]] #number of threads
times=np.zeros((np.size(numthreads),1)) #nparray to save the duration of the compilation for each number of threads
pi=np.zeros((np.size(numthreads),1)) #results of pi calculation
for j in range(np.size(numthreads)):
    p = subprocess.Popen(['./a.out'], stdout=subprocess.PIPE, stdin=subprocess.PIPE) #open run c++ program and save the results

    value=str(numthreads[j][0]) +'\n'+str(numthreads[j][0]) + '\n'
    value=bytes(value, 'UTF-8')  
    result, _ = p.communicate(input=value)    
    # Decode and process the result
    result =result.decode("utf-8").strip().split('\n')
    print(result)
    
    matches = re.findall(r'[\d+\.\d+]+', result[0]) #pi
    pi[j]=float(matches[1])
    
    matches = re.findall(r'[\d.]+', result[1]) #duration
    times[j]=float(matches[0])
#plot duration as a function of number of threads
f=plt.plot()
plt.scatter(numthreads,times)
plt.xlabel('Number of threads')
plt.ylabel('Time in miliseconds')
plt.grid()
plt.savefig('numthreads.png')
plt.close()
#fit Amdahl's law and find p
def Amdahl(s,p):
    y=1/((1-p)+p/s)
    return y

from scipy.optimize import curve_fit
f2=plt.plot()
numthreads=[1,2,4,8,16,32,64]
speedup=np.array([times[0]/times[0],times[0]/times[1],times[0]/times[2],times[0]/times[3],times[0]/times[4],times[0]/times[5],times[0]/times[6]])
speedup=np.ndarray.flatten(speedup)
xdata = np.asarray(numthreads) #prepare xdata and ydata for curve_fit
ydata = np.asarray(speedup)

parameters, covariance = curve_fit(Amdahl, xdata, ydata)
fit_y = Amdahl(xdata, parameters[0])
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xdata, fit_y, '-', label='fit')

plt.xlabel('Number of threads')
plt.ylabel('Speedup')
plt.grid()
plt.legend()
plt.title(f'p={parameters[0]:2.3f}')
#plt.show()
plt.savefig('speedup.png')
plt.close()
