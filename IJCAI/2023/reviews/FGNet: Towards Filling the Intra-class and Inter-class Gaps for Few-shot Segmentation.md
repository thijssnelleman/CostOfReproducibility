
## FGNet: Towards Filling the Intra-class and Inter-class Gaps for Few-shot Segmentation
Yuxuan Zhang, Wei Yang, Shaowei Wang
Keywords: Computer Vision: CV: Segmentation, Computer Vision: CV: Transfer, low-shot, semi- and un- supervised learning
IJCAI/2023/Proceedings/0194 - FGNet: Towards Filling the Intra-class and Inter-class Gaps for Few-shot Segmentation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors share a link to their implementation (https://github.com/YXZhang979/FGNet). In the readme they briefly state an introduction to the method and that most of the code has been released but the rest is to follow (Last commit 6 months ago, accessed on 11-03-2025). Only the dataset code has some comments. The authors share some details on which their method was built upon in section 3. In general the code requires quite some reverse engineering to use for documentation for re-implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors state in section 4 they use two widely used data sets, present citations on them and a description. A data loader for the datasets is present in the code but no details on the data sets themselves. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state a few hyperparameter values / architecture design choices in section 4. Some more could be extracted from the implementation (hard coded) and with some effort it can be checked if all needed values are present. No details are given regarding the acquisition of the hp values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the training/testing split in section 4 of the data. They state the metric (as an acronym) but do not explain it. They state they present the best mean performance over 1 and five shot scenarios on both data sets in section 4.1. Some details would have to be checked but in general this information is quite complete.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries experience with few-shot learning, image segmentation.
