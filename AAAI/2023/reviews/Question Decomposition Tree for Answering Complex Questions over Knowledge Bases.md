
## Question Decomposition Tree for Answering Complex Questions over Knowledge Bases
Xiang Huang, Sitao Cheng, Yiheng Shu, Yuheng Bao, Yuzhong Qu
Keywords: SNLP: Question Answering, KRR: Ontologies and Semantic Web, SNLP: Syntax -- Tagging, Chunking & Parsing
AAAI/2023/Proceedings/26519 - Question Decomposition Tree for Answering Complex Questions over Knowledge Bases.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/cdhx/QDTQA). The authors specify environment details regarding their implementation, where the data can be found, how to set hyperparameter values and how to run the training procedure, how to run predictions and evaluate the results. The repository is rather large, with many different code files. The readme helps a bit with finding your way around. The code has a descent amount of comments. An overview of their method is presented in the paper and implementation details are briefly discussed. However, due to the size of the implementation, a full indexing of the directory structure would be welcome.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

Data is provided in the implementation repository. They use public data sets, provide few statistics on them, and cite their sources. With a bit of digging, independent investigators should have no problem fidning full information required on these data sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

There is some discussion regarding hyperparameters in context of training data collection. No other mention of hyperparameters is made, so they would have to be extracted from the implementation docs.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present the used metrics in their paper with a description. The authors clearly state the training method and how models were determined using checkpoints and validation data. This indicates single model results on the test set, although this is not specifically stated, but can with relative ease be confirmed by using their implementation docs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The authors provide a good entry level introduction to the task with examples. With the extensive implementation details this makes the method easy to get in to, although some external documentation will be required.
