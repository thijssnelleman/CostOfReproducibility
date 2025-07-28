
## Estimating Joint Treatment Effects by Combining Multiple Experiments
Yonghan Jung, Jin Tian, Elias Bareinboim
Keywords: 
ICML/2023/Proceedings/24347 - Estimating Joint Treatment Effects by Combining Multiple Experiments.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

There are a lot of detailed code snippits in the appendix. They state their programming language is Python. They also provides links for dependencies used. This gives a lot of good starting points. However not all the code is given so some parts will have to be filled in. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide a link for the STAR data set in the appendix E. They also provide the source code for their synthetic data generators. The synthetic data generators are described at length in the appendix and sec 5.1. The same holds true for STAR data set in 5.2. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate over a few different estimators. It seems there are no other variables for the method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors split the data into training and test with a 5:5 ratio regarding training and testing in the appendix. But no other note is made of this. The metric is AAE (Average absolute error). The populations are 100 simulations for the simulation, for the STAR data set this is unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires experience in estimators.
