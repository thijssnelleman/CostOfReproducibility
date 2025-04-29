
## Efficient Embeddings of Logical Variables for Query Answering over Incomplete Knowledge Graphs
Dingmin Wang, Yeyuan Chen, Bernardo Cuenca Grau
Keywords: DMKM: Linked Open Data, Knowledge Graphs & KB Completion, DMKM: Applications, DMKM: Semantic Web
AAAI/2023/Proceedings/25588 - Efficient Embeddings of Logical Variables for Query Answering over Incomplete Knowledge Graphs.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their source code in the paper (https://github.com/wdimmy/Var2Vec). The readme provides installation notes (such as requirements) how to download the data and from where, how to download the model, how to train the models (brief), and how to test the method (brief). The code has a descent amount of comment but could do with some more. The repository seems to have some duplicate code too. With a bit of clean up, this should be a 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide download instructions on the data sets in their repository. They state they consider a benchmark data set in their paper with citations. They provide some statistics in table 1 on the data. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide detail on the hyperparameters used in their paper. They can be checked with some effort against the HPs defined in their implementation. No details are provided on how the values were determined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide a seperate section explaining and motivation the metrics used for evaluation. The results are on single models (implied by the paper / results table).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a good understanding on query problems.
