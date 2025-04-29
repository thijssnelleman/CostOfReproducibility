
## A Unified Strategy for Multilingual Grammatical Error Correction with Pre-trained Cross-Lingual Language Model
Xin Sun, Tao Ge, Shuming Ma, Jingjing Li, Furu Wei, Houfeng Wang
Keywords: Natural Language Processing: Applications, Natural Language Processing: Language Generation
IJCAI/2022/Proceedings/0606 - A Unified Strategy for Multilingual Grammatical Error Correction with Pre-trained Cross-Lingual Language Model.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors link two repositories they used for their implementation: One regarding the model and one for evaluation/measurements. They also link a repository used for data augmentation. There is an overview of the method in figure 1 and 2. Their own implementation is not provided.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors state in 3.1 they use three datasets for their method, provide citations on each and summarise the statistics in table 1. The only description on them is that they are "GEC" (Synthetic data construction of Grammatical Error Correction) datasets, and the languages of each. They state these are benchmark datasets in the introduction. No direct links provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors detail the hyperparameters in appendix A. Here they specify the parameters for data construction, the fine-tuning HPs for each dataset and thus a summary in tabular format of the HP space considered. No acquisition method/budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the (static) data splits in table 1. The authors use precision, recall and F0.5 as metrics (stated in 3.1). Only F0.5 is not very standard but can be safely assumed as previous knowledge for the reader. The results are single run (static test set, no folds specified, single numbers in result tables).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in NLP.
