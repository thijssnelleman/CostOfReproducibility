
## Factual and Informative Review Generation for Explainable Recommendation
Zhouhang Xie, Sameer Singh, Julian McAuley, Bodhisattwa Prasad Majumder
Keywords: SNLP: Generation, DMKM: Recommender Systems, PEAI: Interpretability and Explainability, SNLP: Language Grounding
AAAI/2023/Proceedings/26618 - Factual and Informative Review Generation for Explainable Recommendation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a source for their implementation (https://github.com/zhouhanxie/PRAG). In the readme they provide a diagram / poster on their method. They have notes on the implementation and how it should be run, links to the appendix, links to other models they have based theirs on, and a direct link to the used data set. The readme could do with some general introduction of the repository structure however as the code base is rather large, and especially could use direct instructions on how things should be run. The code in general has fewer comments than could have been, which could also limit understandability. The authors provide an overview for the architecture in their paper and some examples.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three publicly available data sets for their experiments, provide citations on them and a short note on the data splits. No other details were provided in the paper, however direct download links were made available in the implementation documentation.  Data set statistics are available in the appendix on the repository.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

There are no details in the paper regarding hyperparameters. There are default hyperparameter values present in the implementation documentation that could be extracted with some effort (No seperate files, have to look at args defintions per CLI entry point). No details are provided on how these values were determined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors provide details on training the (pre-trained) models. The authors state they generate 10,000 sampels per model and evaluate them on three metrics they describe themselves and one more standardised metric. The newly introduced metrics may be some work to grasp/reproduce but are well documented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requries a good understanding of recommender systems.
