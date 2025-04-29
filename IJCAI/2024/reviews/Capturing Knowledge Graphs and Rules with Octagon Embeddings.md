
## Capturing Knowledge Graphs and Rules with Octagon Embeddings
Victor Charpenay, Steven Schockaert
Keywords: Knowledge Representation and Reasoning: KRR: Learning and reasoning, Data Mining: DM: Knowledge graphs and knowledge base completion, Machine Learning: ML: Neuro-symbolic methods
IJCAI/2024/Proceedings/0364 - Capturing Knowledge Graphs and Rules with Octagon Embeddings.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present a theoretical analysis on which they give a model on in section 5 with learnable weights. They reference previous works for parts of this, and define the learnable functions and hyperparmeters and the loss function. The authors have an implementation details section in the supplementary materials which they provide a direct link to. In the supplementary materials a URL is given to the library with which they developped their implementation, followed by a link to their implementation details (https://github.com/vcharpenay/uvxy). In the readme they state how to install the requirements for their code and how to run an experiment, with where the results can be found. The  code has a decent amount of comments, but more documentation would be welcome.


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors state they use two common benchmarks and provide citations on them. However no details on the data set are given nor direct links, leaving it to the independent investigators to determine (or have this as previous experience). There is no clarification in the implementation documentation where this data could be found.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the hyperparameters of their model in section five, and refer for their values to the supplementary materials in section 6. A full table on the hyperparameter values is given for each experiment, summarise them in config files in the implementation and state either where they values have been sourced from or how they had been altered (empirical experience for some, grid search for another and the sizes of these grids).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used for evaluation, which thet state are common in this field. The authors state details on the training procedure in the supplementary, but not all are given such as train/test split. These could be figured out from the implementation with some effort, as it is not directly clear from their eval.py script, it is seemingly handled by the depending library. The results indicate single model/run evaluations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The authors present a theoretical anaylsis of graph embeddings representation, which requires a thorough understanding of graphs/geometric deep learning. Furthermore, many details in the experiments section are assumed as pre-knowledge, such as the metrics definitions, thus raising the bar even further. This is not a negative reflection on the work of the authors, rather it is a complex method meaning expertise is needed to reproduce their work.
