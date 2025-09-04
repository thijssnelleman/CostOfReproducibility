## Understanding the Covariance Structure of Convolutional Filters
Asher Trockman, Devin Willmott, Zico Kolter
Keywords: 
ICLR/2023/Proceedings/10786 - Understanding the Covariance Structure of Convolutional Filters.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors provide a link to their implementation in the abstract (https://github.com/locuslab/convcov). The repository is empty however. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use CIFAR-10 and ImageNet but provide little detail on them.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors provide details on a HP search for both datasets in appendix C. Structured overview of HPs and their values missing and not all values are clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure test set accuracy with three random seeds and presented with avereage + standard deviation. Data split not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
