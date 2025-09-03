## How Does SimSiam Avoid Collapse Without Negative Samples? A Unified Understanding with Self-supervised Contrastive Learning
Chaoning Zhang, Kang Zhang, Chenshuang Zhang, Trung X. Pham, Chang Yoo, In Kweon
Keywords: 
ICLR/2022/Proceedings/6629 - How Does SimSiam Avoid Collapse Without Negative Samples? A Unified Understanding with Self-supervised Contrastive Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[6]

The authors provide detailed and practical pseudocode for their method in algorithm 1-6, using PyTorch. Overviews of the method are given in figure 1 and 2. The implementation is not given. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[8]

(1/1)

The authors present results on CIFAR100 in table 5, but do not provide any information on it at all. For many of the other results, it seems to be using dummy functions (simulators) but the details are really not clear.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors use a pre-existing method and conduct an analysis on it, for which they summarise the values in text in A.1. but no structured overview.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors analyse the training behaviour of the method in most results, using standard metrics such as loss, entropy, cosine similarity and top-1 %. However, in table 5 a result on CIFAR-100 is given, for which it is not specified on what subset it is.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
