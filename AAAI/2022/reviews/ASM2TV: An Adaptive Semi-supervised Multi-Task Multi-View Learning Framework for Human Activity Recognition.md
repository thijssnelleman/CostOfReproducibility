
## ASM2TV: An Adaptive Semi-supervised Multi-Task Multi-View Learning Framework for Human Activity Recognition
Zekai Chen, Xiao Zhang, Xiuzhen Cheng
Keywords: Machine Learning (ML), Search And Optimization (SO), Knowledge Representation And Reasoning (KRR), Reasoning Under Uncertainty (RU)
AAAI/2022/Proceedings/20584 - ASM2TV: An Adaptive Semi-supervised Multi-Task Multi-View Learning Framework for Human Activity Recognition.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/zachstarkk/ASM2TV). A readme is missing. The authors present configuration files for two experiments, and data loading / preprocessing scripts. The code is largely without comments. The documentation could definitely be improved, but all required materials do seem to be present. The authors provide pseudo code on their algorithm, and three illustrations/schematics on their framework. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use two data sets, provide citations on them, and an extensive description. The amount of statistics on the data is relatively few. The authors provide no direct links to the data sets. It is not clearly stated where the data is publicly available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state a few hyperparamter values in their experiment settings, and a full list can very easily be extracted from the implementation docs. They also refer to the supplementary material but that is missing (AAAI limitations). No acquisition method is specified on the hyperparameter values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors have a 'baselines and metrics' scetions but no metrics are introduced there. It will take an experienced eye to dissect the meaning of each metric relative to the setting/task. There is no description on how the data is divided for training / testing or whether this is not done at all. This information is either missing or requires more task specific expertise to understand.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

This method requires expertise on the task to understand the experiment presented, as well as some experience on all the subdomains the paper covers (see keywords) as it is a very layered process. The implementation documentation could have made up a part of this.
