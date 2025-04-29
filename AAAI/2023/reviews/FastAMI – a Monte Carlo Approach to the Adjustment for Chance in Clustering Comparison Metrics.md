
## FastAMI – a Monte Carlo Approach to the Adjustment for Chance in Clustering Comparison Metrics
Kai Klede, Leo Schwinn, Dario Zanca, Björn Eskofier
Keywords: ML: Clustering, ML: Probabilistic Methods
AAAI/2023/Proceedings/26003 - FastAMI – a Monte Carlo Approach to the Adjustment for Chance in Clustering Comparison Metrics.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/mad-lab-fau/fastami-benchmark). In the readme they provide installation and compilation notes, as well as some details on which the implementation is based. They provide a zip for the data and instructions on where to place it. They give instructions on how to execute the benchmarks. The code has a good amount of comments and clear remarks when it was lend from another source. In general the implementation is very well documented. A pip installation is also available on the method. Pseudo code on the method is given in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(11/11)

The authors use two data sets, on the first they provide a zipfile, citations and some key properties. The second cited source provides 8 datasets with small description, but not provided in the implementation. So to re-use the second data set will be some effort. Moreover they generate synthetic data on which the sampling is described in the paper and the code is provided in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method explores different parameter values. They present these in their work with visualisations and is seemingly a grid search. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The auhtors describe the methods eva;luated on the benchmarks, the metrics recorded (runtime). They conduct a search of parameter values which is also clearly presented. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

An understanding of graph clustering and the MC method is needed.
