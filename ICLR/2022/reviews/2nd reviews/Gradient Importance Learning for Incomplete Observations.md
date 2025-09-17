## Gradient Importance Learning for Incomplete Observations
Qitong Gao, Dong Wang, Joshua Amason, Siyang Yuan, Chenyang Tao, Ricardo Henao, Majda Hadziahmetovic, Lawrence Carin, Miroslav Pajic
Keywords: 
ICLR/2022/Proceedings/6859 - Gradient Importance Learning for Incomplete Observations.pdf
Project URL: nan


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation online (https://github.com/gaoqitong/gradient-importance-learning/tree/main/sequential_data). The repo contains sufficient info to install and run the code. More than 50% of the code is not commented, or the comments are not sufficiently expressive and informative (this increases the score by 1). Te repo structure is very simple and easy to navigate, as the authors essentially provide scripts for running their experiments, and not a classical Python package aimed to be imported and used in other works.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/4)

Each dataset is described in detail in the Appendix, along with a direct link and citation, as well as dataset statistics. Only one dataset is private, containing confidential medical information. However, even the private dataset is thoroughly described, and the Github repo states that the data is available upon request. Total cost increases by 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[6]

The hyperparameter space is stated in the Appendix, without an overview (cost increases by 1). Final hyperparameter values are not provided in the paper nor the repo (cost increases by 3). Hyperparameters were tuned via grid search with unknown budget (cost increases by 1).

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The evaluation metrics very common (accuracy, AUC). The train/test split of the data is not clearlt specified in the paper, however in the repo the authors state that for some datasets the training data is available upon request. This does not yield sufficiently clear information for reproducibility, although many details are there. Strategy is also not clear (+2). The results are averages and std is reported.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

Even though most details are already available, even if we simply want to rerun their implementation in the hope of getting the same results, we need to at least contact the authors for training data, and we lack knowledge about the final configuration of the models being deployed at test time. If we want to independently put the pieces together, we still lack crucial details on the experimental protocol, namely train/test splits, strategy details... therefore a relatively high score.
