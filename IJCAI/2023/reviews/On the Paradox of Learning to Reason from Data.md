
## On the Paradox of Learning to Reason from Data
Honghua Zhang, Liunian Harold Li, Tao Meng, Kai-Wei Chang, Guy Van den Broeck
Keywords: Knowledge Representation and Reasoning: KRR: Learning and reasoning, Natural Language Processing: NLP: Interpretability and analysis of models for NLP, AI Ethics, Trust, Fairness: ETF: Trustworthy AI
IJCAI/2023/Proceedings/0375 - On the Paradox of Learning to Reason from Data.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/joshuacnf/paradox-learning2reason). In the readme they state an overview of what code they provide, the environment the code was ran in, how to evaluate the model for section 2.2, how to regenerate the datasets used for the experiment, and examples for executing training and evaluation for two models. The code has an okay amount of comments but could be organised a bit better, but the file structure is very overseeable. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors produce their own data, implementation of which is available in their repository with instructions on how to generate with their original generation scripts. They procedures are described in section 3.1. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors use a pretrained model and train it on their data sets. The hyperparameters of this are only briefly discussed in 2.2, and most values will have to be extracted from the implementation docs. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the data is split in training/validation test in 3.2 but not with which proportions which would have to be extracted from the implementation. The authors present test set accuracy as results with single run/models. They show the results over various reasoning depths. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires an understanding of NLP and BERT as well as the task (reasoning for AI).
