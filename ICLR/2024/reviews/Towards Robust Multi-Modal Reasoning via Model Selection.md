## Towards Robust Multi-Modal Reasoning via Model Selection
Xiangyan Liu, Rongxue LI, Wei Ji, Tao Lin
Keywords: 
ICLR/2024/Proceedings/18902 - Towards Robust Multi-Modal Reasoning via Model Selection.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

Authors provide a link to their implementation in the abstract (https://github.com/LINs-lab/M3). The readme has installation notes, how to run the code examples, and notes on the reproducibility. Code has okay comments. Structure needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

MS-GQA, a dataset the authors created by modifying a previous one (cited) and is briefly described in section 4.1. Construction and details given in appendix A. Dataset available in the implementation including code. Few statistics provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors state a grid search for some parameters in appendix C. Structured overview missing, although most parameters can be deduced from code with a bit of effort.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Evaluation metrics stated in section 4.2. Results are over 5 random seeds on the test set, data split in appendix a. Agg/var not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
