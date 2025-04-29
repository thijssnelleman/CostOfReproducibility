
## Computational Modelling of Quantifier Use: Corpus, Models, and Evaluation
Guanyi Chen, Kees van Deemter
Keywords: 
JAIR/2023/Proceedings/13899 - Computational Modelling of Quantifier Use: Corpus, Models, and Evaluation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide two links in footnote 4 of the introduction and state a link to the dataset, and one to their code (https://github.com/a-quei/quantified-description-generation). Code can use more comments. No installation notes, although the authors only seem to use Python standard libraries the Python version would help. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors discuss the dataset acquisition in 2.2, including annotator setup, with various examples, statistics (table 1/2/3), and lengthy descriptions. The data set is available online and a link is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state their method in algorithm 1/2. All parameters are input related.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method in table 6 in 'Naturalness', 'Informativity' and 'Correctness' for human jugdements which is described in 4.1. and the results are averaged over 4 annotators. For 4.2. they evaluate SWAP score (eq. 1) and use a population of 29 humans for the evaluation and describe the process.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on NLP and human evaluation.
