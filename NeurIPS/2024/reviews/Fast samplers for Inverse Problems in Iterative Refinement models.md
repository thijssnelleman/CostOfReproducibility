
## Fast samplers for Inverse Problems in Iterative Refinement models
Kushagra Pandey, Ruihan Yang, Stephan Mandt
Keywords: 
NeurIPS/2024/Proceedings/93464 - Fast samplers for Inverse Problems in Iterative Refinement models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]


The authors provide a link to their implementation (https://github.com/mandt-lab/c-pigdm). In the readme they introduce the method with some examples, how to setup for the code with dependencies, setting up pretrained checkpoints, how to manage the configurations, where to find example scripts that they used to produce results. The repository structure is very large and needs an index. The code has fine comments. An overview is given in figure 1, pseudo code in algorithm 1. Design choices are presented in sec 2.2.2.
### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors state the pretrained models and datasets used in section 3. The dataset is FFHQ (citation given). The dataset automatically downloads in the code. No description or statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors conduct an ablation study on three hyperparameters in section 3.3, which they choose based on their theoretical insights from sec 2.3. The auhtors state a grid search in d.8. over some parameters. No full overview of selected values per experiment can be found.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the task and metrics in sec 3 with citations (Not explained) and some practical notes are given in D.7. The results are single runs. Train/test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on diffusion/flow models and computer vision. 
