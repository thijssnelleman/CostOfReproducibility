
## Learning Fair Representations for Recommendation via Information Bottleneck Principle
Junsong Xie, Yonghui Yang, Zihan Wang, Le Wu
Keywords: Data Mining: DM: Recommender systems, AI Ethics, Trust, Fairness: ETF: Fairness and diversity, Data Mining: DM: Collaborative filtering, Machine Learning: ML: Representation learning
IJCAI/2024/Proceedings/0273 - Learning Fair Representations for Recommendation via Information Bottleneck Principle.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/jsxie9/IJCAI_FairIB). In the readme the authors provide an introduction to the method and how to run the training for two data sets. The code is mostly without comments. The repository is not too large, reducing the impact of the lack of documentation of their code, yet it is still substantial.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors provide .pkl files of two data sets in their implementation source. The authors provide citations on the data sets in their work, with some statistics on them in table 1. General descriptions are missing, which would have to be extracted from the citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the values of the hyperparameters in the implementation details, but not how they were acquired. An ablation study is done in section 5.3 on a few hyperparameters. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use two types of metrics, and for each they describe them, provide citations and for one detailed formulas. They state they repeat the experiment 10 fold and report the averages. The authors state how the data is divided for training/testing, and seem to indicate a fixed split but this would have to be verified by following a citation they give.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires previous experience with recommender systems, but in general each topic is well introduced, lowering the expectation of having to rely on other sources to reproduce the work.
