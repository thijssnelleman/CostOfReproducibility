
## Speeding Up Multi-Objective Hyperparameter Optimization by Task Similarity-Based Meta-Learning for the Tree-Structured Parzen Estimator
Shuhei Watanabe, Noor Awad, Masaki Onishi, Frank Hutter
Keywords: Machine Learning: ML: Hyperparameter optimization, Machine Learning: ML: Automated machine learning, Machine Learning: ML: Meta-learning
IJCAI/2023/Proceedings/0487 - Speeding Up Multi-Objective Hyperparameter Optimization by Task Similarity-Based Meta-Learning for the Tree-Structured Parzen Estimator.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/nabenabe0928/meta-learn-tpe). In the readme they state installation instructions, how to download the benchmark data set and how to run an example. Some of the code has very good comments, but many files are completely without. The file structure is rather large and is not explained/indexed in the readme, increasing the effort to understand the process/flow. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors state download instructions for a benchmark data set in the implementation docs. In 5.1 they state they use four benchmarks with a citation. The download instruction seems to cover all these datasets. The authors give detailed descriptions in appendix C.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method presented is on hyperparameter optimisation. They state the initialisation and technique details for each experiment in 5.1. Full settings of the meta learning can be found in the appendix.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they optimise two metrics in 5.1. They state under which circumstances the methods are optimised on the data sets. The experiment is a bit layered due to the subdomain but its explained in detail and the implementation docs + appendix lower this cost as much as can be expected.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in HPO.
