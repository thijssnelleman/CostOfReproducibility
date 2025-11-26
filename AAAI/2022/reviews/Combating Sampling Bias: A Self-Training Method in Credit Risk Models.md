
## Combating Sampling Bias: A Self-Training Method in Credit Risk Models
Jingxian Liao, Wei Wang, Jason Xue, Anthony Lei, Xue Han, Kun Lu
Keywords: Credit Risk, Self-training, Reject Inference
AAAI/2022/Proceedings/21528 - Combating Sampling Bias: A Self-Training Method in Credit Risk Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide any details on their implementation. Flowchart overviewing the method in figure 2 and 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[9]

(0/1)

The data used is not public. The authors provide a lengthy introduction/description of the data and certain statistics are provided, however many key details are missing such as actual data set size, features / columns (although some are provided, they simply state 'hundreds of features') of the data which makes it very difficult to defend comparability to another data set.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state tehy use Amazon Sagemaker with Bayesian search to tune the hyperparameters of their model. It is not specified how this is done, what the result is or what budget was used.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The author describe their evaluation metrics and provide citations on them. They state the test set is fixed across metrics. There is a brief statement on how the data set was split into training and testing, however more information would be needed to ensure a representative experiment. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The method requires some understanding of data statistics and processing/augmentation, the applied models are straightforward. A general understanding of the task can help.
