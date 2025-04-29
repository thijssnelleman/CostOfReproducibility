
## A Data Source for Reasoning Embodied Agents
Jack Lanchantin, Sainbayar Sukhbaatar, Gabriel Synnaeve, Yuxuan Sun, Kavya Srinet, Arthur Szlam
Keywords: ML: Applications, ML: Relational Learning, ML: Representation Learning, SNLP: Applications, SNLP: Language Grounding, SNLP: Other Foundations of Speech & Natural Language Processing, SNLP: Question Answering
AAAI/2023/Proceedings/26017 - A Data Source for Reasoning Embodied Agents.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/facebookresearch/neuralmemory). They provide installation notes and a script on how to generate data with explanation. They link/submodule another repository called FAIRO. The code is relatively comprehensive to browse through and contains a decent amount of comments. As the paper presents the data generation as the method, this is sufficient, although the readme could be extended with more information.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The method is regarding data generation. The authors present details on the data regarding a data loader, and data generation. There is a clear explanation on the data generation in the method and what the structure looks like. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The configuration of the data generation is given in the implementation docs. Complete files can be found there in a structured manner. The authors also provide the hyperparameter values of methods trained on their data, although this is not the main focus of the paper. They also share details on their grid search for those values. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors detail the metrics used for evaluation over 4 different data set types. The authors describe results for single models. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The method requires a good understanding of data generation and the task at hand, to understand the configurable data generation concept. The method is very well documented, with many examples and ease-of-use implementation is readily available, making it easier to grasp and reproduce the method.
