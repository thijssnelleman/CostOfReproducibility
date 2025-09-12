
## Exploring Example Influence in Continual Learning
Qing Sun, Fan Lyu, Fanhua Shang, Wei Feng, Liang Wan
Keywords: 
NeurIPS/2022/Proceedings/55328 - Exploring Example Influence in Continual Learning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation in the subtitle (https://github.com/SSSunQing/Example_Influence_CL). Installation requirement given but are seemingly incompelte in the readme and an overview on the code. Code has okay comments. Overview in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors state 3 datasets (split CIFAR-10, CIFAR-100 and Mini-Imagenet) with citation and a small description. No direct links or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors refer to a previous work for hyper-parameters. They are not given except for the number of epochs. Some can be deduced from the code, but in general most information is not presented here.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metrics are defined with formulae in 6.1. Dataset split is 80/20 t/t randomly. All results are averaged over 5 runs (std in appendix) with random (but fixed) seeds. The authors evaluate testing performance.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on continual learning.
