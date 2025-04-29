
## DANet: Image Deraining via Dynamic Association Learning
Kui Jiang, Zhongyuan Wang, Zheng Wang, Peng Yi, Junjun Jiang, Jinsheng Xiao, Chia-Wen Lin
Keywords: Computer Vision: Computational photography, Computer Vision: Applications, Computer Vision: Other
IJCAI/2022/Proceedings/0137 - DANet: Image Deraining via Dynamic Association Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. They do state/cite a paper in 3.1 of which they use the 'publicly released codes' for 'tuning the optimal settings', giving some starting point for the independent investigators but no links to this are provided. No practical details are shared. Their framework is presented in figure 3. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4] 

(8/8)

The authors state they use a public data set for training with their specified procedure, test on four synthetic benchmarks and three real world data sets (implied public based on the sentence). On each a citation is provided. The training set has one statistic stated. No statistics or descriptions are provided in general. No direct links provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors state various hyperparameter values in 3.1. A total overview of the hyperparameter space is missing. No acquisition strategy/budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the five metrics used in section 3, with an explanation of each acronym and some citation, but details/formulas are not given increasing the subdomain knowledge required for setting up the experiment. The authors clearly state which datasets are used for training and which for testing. The results are single run/model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires previous experience with CV/Deraining task. The missingimplementation complicates this.
