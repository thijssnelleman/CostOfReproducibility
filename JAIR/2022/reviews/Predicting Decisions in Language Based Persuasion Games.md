
## Predicting Decisions in Language Based Persuasion Games
Reut Apel, Ido Erev, Roi Reichart, Moshe Tennenholtz
Keywords: 
JAIR/2022/Proceedings/13510 - Predicting Decisions in Language Based Persuasion Games.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract, footnote 1 (https://github.com/reutapel/Predicting-Decisions-in-Language-Based-Persuasion-Games). In the readme they state the abstract of the paper. There are no installation instructions. The code has good comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors collect their own data and state the process regarding human input in 4.1. They analyse the data in 4.2. and dataset is available in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors define hyperparameters and architecture types in section 6. Overview in figure 8 for LSTM models. Hyperparameter values are summarised per experiment in an .xlsx file. The authors take the architectures from their original methods and is available in the code albeit a bit difficult to read. There are also grid searches defined in the code per method / hyperparameter.  In 7.3. this process is stated (six-fold cross-validation) but not which values are selected.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use six-fold cross validation and report results on the test set with accuracy and F1-score, and report the averages. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on NLP.
