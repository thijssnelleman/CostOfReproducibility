
## Imperceptible Backdoor Attack: From Input Space to Feature Representation
Nan Zhong, Zhenxing Qian, Xinpeng Zhang
Keywords: Computer Vision: Adversarial learning, adversarial attack and defense methods, AI Ethics, Trust, Fairness: Trustworthy AI
IJCAI/2022/Proceedings/0242 - Imperceptible Backdoor Attack: From Input Space to Feature Representation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/Ekko-zn/IJCAI2022-Backdoor). In the readme they state instructions on how to run the code for training and evaluation, a requirement/dependency and direct links to the two datasets and trained models. The code has almost no comments. The repository is small and thus easy to oversee. An overview of the framework is given in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors provide direct links to the datasets in their implementation. They state the datasets in 4.1 with citations and descriptions and some minor statistics which can be more detailed.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in the training details paragraph of 4.1. The space considered is ducmented in the implementation config.py file with default values which can be assumed for any missing specifications. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the train/test split in in 4.1, which is statically decided in each dataset. The metrics are accuracy and L1 norm distortion for which they provide a formula. The results are singular.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in CV and adverarial learning.
