
## Cross-domain Constituency Parsing by Leveraging Heterogeneous Data
Peiming Guo, Meishan Zhang, Yulong Chen, Jianling Li, Min Zhang, Yue Zhang
Keywords: 
JAIR/2024/Proceedings/15736 - Cross-domain Constituency Parsing by Leveraging Heterogeneous Data.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide a link to their implementation in the introduction footnote 2 (https://github.com/guopeiming/CD_ConsParing_HeterData). The repository is empty and the authors state 'We will release the code as soon as the paper is officially accepted'. The authors link a package used for evaluation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(11/11)

The authors state the datasets used in 4.1. PTB, MCTB as well as Wizard, Reddit, ECtHR, Gutenberg (link) and amazon all with citations. For knowledge transfer they use CoNLL03, restaurant, ccgbank, EWT also all with citations. No other details given on the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparameters used in 4.1. No acquisition specified. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Rhe authors use Precision, Recall and F1 score and present the results on three different seeds and report the average. The authors present zero-shot and few-shot results (10,20 and 50).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on NLP.
