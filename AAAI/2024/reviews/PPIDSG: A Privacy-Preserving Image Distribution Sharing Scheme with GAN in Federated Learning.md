
## PPIDSG: A Privacy-Preserving Image Distribution Sharing Scheme with GAN in Federated Learning
Yuting Ma, Yuanzhi Yao, Xiaohua Xu
Keywords: ML: Privacy, ML: Distributed Machine Learning & Federated Learning
AAAI/2024/Proceedings/30527 - PPIDSG: A Privacy-Preserving Image Distribution Sharing Scheme with GAN in Federated Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide their source code implementation on GitHub (https://github.com/ytingma/PPIDSG). The repository includes a diagram of the method, a setup section regarding dependencies, a table of data sets with download links and application details, a table of 5 baselines with paper links and code links. They list the hyperparameter settings per attack/model/dataset (albeit a bit confusing) and a short description where you can execute the attacks. There is a short description on how to train their model. There are a couple of notes to help you along the way. The repository feels a bit vague in its structure, although there are some comments in the code to help you along the way, and the authors clearly made an effort to document. There are also a few details on the implementation in the paper, including an overview of the framework and pseudo code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use four data sets for their experiments, all of which have citations and clear download links in their implementation documentation. Metrics on the data sets are not given. Data loading is available in their implementation docs. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameter values are clearly documented in the implementation documentation, and also shortly presented in the paper. There are no details or explanations on how these values were acquired. There is some exploration regarding activation functions presented in table 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The exact procedure is not clearly stated in the paper, but given the results tables it seems to indicate single runs of the framework. The metrics stated are accuracy and thus straightforward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method covers many different topics and analyses quite a few different angles, on generative adverserial networks, federated learning and privacy preservation. It will require some knowledge to understand the method, but the extensive documentation provided by the authors definetily lowers this threshold.
