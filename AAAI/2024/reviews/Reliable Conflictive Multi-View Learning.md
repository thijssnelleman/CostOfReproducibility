
## Reliable Conflictive Multi-View Learning
Cai Xu, Jiajun Si, Ziyu Guan, Wei Zhao, Yue Wu, Xiyue Gao
Keywords: ML: Multi-instance/Multi-view Learning, ML: Multi-class/Multi-label Learning & Extreme Classification, ML: Multimodal Learning, ML: Representation Learning
Award: Outstanding paper award
AAAI/2024/Proceedings/30911 - Reliable Conflictive Multi-View Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors published their code on GitHub (https://github.com/jiajunsi/RCML). There they summarise the results of their work and illustrate the model with an example. However the authors do not provide instruction on how to use their code in the README and the code also lacks comments, increasing the effort to understand what happened.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors provide three datasets on their GitHub, including a data loader (albeit nearly without supporting documentation). In their paper the authors give a clear data set summary, and although not each data set can be found on the GitHub the authors clearly link the sources in their paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors do not specify any hyperparameters except for the view, they do clearly explain the loss function (semantic parameters) of their method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors explain their experimental set up and how many times it was repeated, but leave out for example what 'portion' of the data was used for test set. From the code it could be deduced that its 20%, but clearly stating it would help.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method seems to be a quite complex concept, where the study of the mathematical notation to fully grasp what is happening would take some investment from independent investigators. The authors support their work with examples, illustrations and a clear problem statement which should support the learning curve of independent investigators.
