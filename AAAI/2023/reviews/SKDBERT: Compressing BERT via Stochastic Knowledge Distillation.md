
## SKDBERT: Compressing BERT via Stochastic Knowledge Distillation
Zixiang Ding, Guoqing Jiang, Shuai Zhang, Lin Guo, Wei Lin
Keywords: ML: Learning on the Edge & Model Compression, CV: Learning & Optimization for CV, CV: Representation Learning for Vision, SNLP: Language Models, SNLP: Learning & Optimization for SNLP, SNLP: Text Classification
AAAI/2023/Proceedings/25902 - SKDBERT: Compressing BERT via Stochastic Knowledge Distillation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors state implementation details can be found in the appendix which they link to. Although it is not a link to their implementation, they do provide the source repository for it (https://github.com/google-research/bert) and supply us with vast details regarding the architecture, loss functions and many more. It will still be some work to re-implement this, however with this amount of detail given, independent investigators will have a clear roadmap on how to do so.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use the GLUE benchmark with citations on each data set and dissect each task in the supplemantary materials. Statistics on the data sets seem to be missing. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide details on their hyperparameters in the supplementary materials (https://arxiv.org/pdf/2211.14466.pdf). They state the hyperparameter they considered for finetuning and the grids they evaluated them on.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics used are stated in the results table and are straightforward, and more extensive details on them can be found in the supplementary materials. The results are single model (pretrained).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method requires a good understanding on LLMs and how models can be pruned/trimmed into smaller models whilst retaining their performance. 
