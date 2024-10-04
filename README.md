## OpenMP: Estimation of $\pi$ using Monte Carlo

The aim of this project is to estimate the value of $\pi$ using a Monte Carlo method and parallel programming techniques. 
The Monte Carlo method offers a numerical approach for integration by randomly sampling points and assessing how many of those points fall inside a defined geometric shape. In this case, we are approximating $\pi$ by evaluating the area of a quarter circle inscribed in a unit square. To calculate $\pi$, the following relationship between the area of the quarter circle and the area of the square is used:
$$
    \pi=\frac{4 E}{r^2}
$$

where $E$ represents the area estimated using Monte Carlo integration, and $r$ is the radius of the circle. For simplicity, we set $r = 1$.\par

In addition to implementing this calculation, multi-threading programming was introduced to speed up the Monte Carlo method, as the algorithm inherently involves a large number of independent computations.
Additionally, the speedup of the program was evaluated and fitted with a curve based on Amdahl’s law, which predicts the theoretical maximum speedup achievable depending on the proportion of the code that can be parallelized.
Furthermore, a convergence study was conducted by fitting a line to the log-log plot of the relative error in estimating $\pi$ versus the number of points used, highlighting the relationship between the number of points and the accuracy of the Monte Carlo method.

The program was run on the Aristotelis cluster of the Aristotle University of Thessaloniki, which has 64 available threads. The files that run on the cluster were the C++ and Pyhton ones.
The jupyter-noteooks concern the compilation of the method to a common personal computer with 8 threads, and analyticaly include the results.
