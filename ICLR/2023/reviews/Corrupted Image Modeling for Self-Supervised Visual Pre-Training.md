## Corrupted Image Modeling for Self-Supervised Visual Pre-Training
Yuxin Fang, Li Dong, Hangbo Bao, Xinggang Wang, Furu Wei
Keywords: 
ICLR/2023/Proceedings/11664 - Corrupted Image Modeling for Self-Supervised Visual Pre-Training.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors refer to the code base of a previous paper, which can serve as a good starting point. Overview in figure 1.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

ImageNet-1K, Citation provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

HP values reported in tables 13-15 per experiment. For fine tuning they refer to a previous work.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

They measure mIoU, top 1 acc, with median over 3 independent runs. Data split not clear nor which is reported on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
