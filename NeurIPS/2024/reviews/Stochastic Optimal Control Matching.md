
## Stochastic Optimal Control Matching
Carles Domingo i Enrich, Jiequn Han, Brandon Amos, Joan Bruna, Ricky T. Q. Chen
Keywords: 
NeurIPS/2024/Proceedings/93135 - Stochastic Optimal Control Matching.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/facebookresearch/SOC-matching). In the readme they describe the method, provide installation instructions and how to run the algorithms with arguments and visualise the results for specific experiments. The comments can be a bit cryptic. The structure is overseeable. In algorithm 2 they provide pseudo code on the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors consider 4 control problems for which they provide citations and state the formulae in appendix F.1. with their parameters. The code for it is given in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide a configuration file including parameter settings in the implementation as well as how to run the code for specific experiments with parameter arguments. Model architectures discussed in F.2 and parameter values in F.1. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics in appendix F.1. and state they compute it by sampling ten batches every 10 training iterations and update using the average with an EMA coefficient 0.02 or 0.01. In figure 1 they state the error bars are std and the metric is control objective estimate. In figure 2/3 they evaluate control L2 error (as explained partially in F.1.) and no variation (only aggregation) as specified in the appendix. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on optimal control problems.
