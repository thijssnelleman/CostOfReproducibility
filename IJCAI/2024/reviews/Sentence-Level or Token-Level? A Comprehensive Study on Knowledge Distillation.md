
## Sentence-Level or Token-Level? A Comprehensive Study on Knowledge Distillation
Jingxuan Wei, Linzhuang Sun, Yichong Leng, Xu Tan, Bihui Yu, Ruifeng Guo
Keywords: Natural Language Processing: NLP: Machine translation and multilinguality, Natural Language Processing: NLP: Interpretability and analysis of models for NLP, Natural Language Processing: NLP: Other, Natural Language Processing: NLP: Summarization
IJCAI/2024/Proceedings/0722 - Sentence-Level or Token-Level? A Comprehensive Study on Knowledge Distillation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors do not share their implementation. However, they do directly link three sources/libraries/implementations they used for their experiments. Section 4.2 contains a few details on how the implementation was done, figure 1 has a high level architecture view. The linked sources used do lower the cost of re-implementation, however the absence of their own still has a substanial impact as many details/decisions by the authors could be determined from it.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(4/4)

The authors use four data sets for their experiments, provide short descriptions on them and some statistics. No citations or links are provided, so the independent investigators will have to determine where/if these data sets are available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The presented method is an analysis of token levels in NLP, there is no algorithm presented that is configurable, however they do apply noise to the task for which they provide details and proportions on in the experimental setup. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state their three types of noise introduction for the experiments, note they use BLEU as a metric (which does require NLP experience, as it is not explained). There is no training/testing procedure specified as the method does not have a training process.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires a thorough understanding of NLP to understand the task.
