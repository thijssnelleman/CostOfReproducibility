
## Collaboration of Experts: Achieving 80% Top-1 Accuracy on ImageNet with 100M FLOPs
Yikang Zhang, zhuo chen, Zhao Zhong
Keywords: 
ICML/2022/Proceedings/17451 - Collaboration of Experts: Achieving 80% Top-1 Accuracy on ImageNet with 100M FLOPs.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state implementation details in 4.1. None of these are practical. Figure 1,2 and 3 give an overview of the method and figure 3 of the architecture.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The authors use imagenet as the data set. No details given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors psecify training parameter values in appendix B.1. No full summary or acquisition method specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure accuracy and FLOPs as metrics. Results are single model. Train test split not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise in large model for CV and model ensembling.
