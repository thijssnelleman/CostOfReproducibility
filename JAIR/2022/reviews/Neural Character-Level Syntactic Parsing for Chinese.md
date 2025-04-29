
## Neural Character-Level Syntactic Parsing for Chinese
Zuchao Li, Junru Zhou, Hai Zhao, Zhisong Zhang, Haonan Li, Yuqi Ju
Keywords: 
JAIR/2022/Proceedings/13052 - Neural Character-Level Syntactic Parsing for Chinese.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors link their implementation in footnote 14 of section 5 (https://github.com/bcmi220/ccharpar). In the readme they state installation requirements, how to run the training script. The code could use some more comments and the structure an index. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use CTB5 and link the code used for processing. They do not provide citations/descriptions/statistics. The compiled dataset is available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Quite some hyperparameters are listed in src/main.py. The architecture is stated informally in 5.1. as well as the hyperparameter values and these seem to be different from the code. Thus, no structured overview, and some parameters choices are not motivated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the CTB5 t/v/t split in 5.1. The authors measure F1 score and Labeled Attachment Score and lin kthe library used for evaluation. The results are over different delta_H over the dev set in fig 11. In table 7 they also measure Accuracy, LR, LP (not defined) and Unlabeled Attachment Scoer (UAS) as well on the SCDT test set, table 8 the same for ZCTB test set. Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on NLP.
