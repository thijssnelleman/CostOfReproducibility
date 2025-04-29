
## Induced Model Matching: Restricted Models Help Train Full-Featured Models
Usama Muneeb, Mesrob I Ohannessian
Keywords: 
NeurIPS/2024/Proceedings/94001 - Induced Model Matching: Restricted Models Help Train Full-Featured Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/uicdice/imm-logistic-regression). In the readme they introduce the method and link other repos regarding implementation, a quick start wit hdescription on how to run the code, notes on the parameter/configuration values, how to train and test the baselines and various examples/configurations, how to visulaise the results and how to obtain schedules. The code has a lot of comments. The repository structure is quite large and no index is given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/2)

For the toy example the authors use synthetic data over a generated cube and explain it in details in 7.1 and state a parameter value of alpha. Data generator provide in the code (datagen.py). The authors also conduct language modeling experiments in 7.2. for which they state the name of the dataset in table 1 caption, and cite two papers regarding the modification but not the source. No other details regarding this dataset are given at all, neither in the implementation. In 7.3 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

Parameter details are stated in appendix D.2.2. There is a note of a delta hyperparameter in equation 8. This has notes on tuning in D.1.1. An evaluation of delta = 1.5 is done in table 4. The authors state in B.2. that tuning delta is optional for their method. The authors set the value of hyperparameter alpha to 1 for all experiments (empirically). In figure 6 a learning rate is also introduced. Luckily there is an overview in their code (train_and_test.py) with an argparse of all considered hyperparmaeters. These have default values. A clear acquisition strategy is not found nor the selected values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use a toy example in 7.1. They refer to figure 1 where they present the results as test accuracy over 300 runs with 10th-90th percentile (averaging implied in the plot). The authors evaluate in table 1 the preplexity (not defined) on the validation and test set of the data set (no splits given) and the aggregation is max selection over the restarts (no variation). In table 2 they evaluate using MCC, F1 score and accuracy (all pretty standard), and report the averages but the variation is not defined. In figure 2, details givein in D.3. they evaluate average reward of a simulated environment averaged over observation length 50 and 30 roll outs where the variation is 10th and 90th percentiles. This gives over the four experiments 1 + 4 + 3 + 1 / 4 and rounded up because I think the tabular experiments are bit more important than the RL experiment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on ML model matching and logistic regression. 
