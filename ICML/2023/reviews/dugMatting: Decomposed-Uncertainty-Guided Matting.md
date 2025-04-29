
## dugMatting: Decomposed-Uncertainty-Guided Matting
Jiawei Wu, Changqing Zhang, Zuoyong Li, Huazhu Fu, Xi Peng, Joey Tianyi Zhou
Keywords: 
ICML/2023/Proceedings/25052 - dugMatting: Decomposed-Uncertainty-Guided Matting.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide an illustration on the framework in figure 2/3 and pseudo code in algorithm 1. Implementation details are stated in 4.1. The implementation is available online (https://github.com/Fire-friend/dugMatting). In the readme they state installation instruction, how to parametrise the code. The code is a bit messy with redundant or chaotic comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use two datsets for their experiments and provide citations on them. They also state key statistics and brief descriptions. For one they provide a download link in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

There are configuration files in the implementation per method / architecture. The authors summarise the implementation details with hyperparameter values in 4.1. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors specify the metrics used in 4.1.  The results are single runs. The data sets contains static splits for training and testing.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries experience with CV to remove sections from images.
