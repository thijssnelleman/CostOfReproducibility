
## CARLANE: A Lane Detection Benchmark for Unsupervised Domain Adaptation from Simulation to multiple Real-World Domains
Bonifaz Stuhr, Johann Haselberger, Julian Gebele
Keywords: 
NeurIPS/2022/Proceedings/55700 - CARLANE: A Lane Detection Benchmark for Unsupervised Domain Adaptation from Simulation to multiple Real-World Domains.pdf
Project URL: https://carlanebenchmark.github.io

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors link their code in the project URL given in the abstract (https://github.com/juliangebele/CARLANE/tree/master/CARLANE%20Baselines). In the readme they link to the project page, dataset and a tutorial, the four baselines and show the results. There are readmes installation instructions per baseline. The code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors publish an new dataset in this work. The acquisition/creation is detailed in section 3 and 4. Statistics in table 1. They link the dataset in their paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors evaluate various baselines and summarise the HPS and their values in table 2. There are also full config files available per baseline in the implementation. They state these are optimized hyperparameters but not how this was done.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors define the metrics in 5.1. The results are reported on the test set, the dataset provides static splits. Results are over 5 runs but aggregation / variation is not defined.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on CV benchmarking.
