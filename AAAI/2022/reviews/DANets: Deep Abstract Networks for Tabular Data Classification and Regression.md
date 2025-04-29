
## DANets: Deep Abstract Networks for Tabular Data Classification and Regression
Jintai Chen, Kuanlun Liao, Yao Wan, Danny Z. Chen, Jian Wu
Keywords: Data Mining & Knowledge Management (DMKM)
AAAI/2022/Proceedings/20309 - DANets: Deep Abstract Networks for Tabular Data Classification and Regression.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/WhatAShot/DANet). In the readme they state an introduction + archticture schematic of the method, direct links to where the data can be found and how it can be converted to be used for their method. They provide installation instructions, how to run the training and inference procedures and how to configure these with explanation of each parameter value. The code cites sources for which pieces of codes are borrowed from where, and has a varying amount of comments per file. A large section in the paper is dedicated to explain the implementation details. In general there is some room for improvement but with the extensive details in the readme, the authors have provided a very solid implementation documentation for re-implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(7/7)

The authors use seven open source data sets for which they provide citations, descriptions/statistics (table 1) and refer to their (missing) appendix for more information. Direct download links are available in the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide a full description on each hyperparameter in their implementation documentation including configuration files for each task.  The authors state for a few hyperparameters/methods 'default' values are used, and for some they apply the Hyperopt library to acquire them with an explanation under which conditions / budgets they are acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state most of their datasets in the experiments provide their own train-test splits and that they are fixed in each experiment. They used official valdiation sets if given and those that didnt they provide a sampling method on how they acquired it from the training sets. They briefly state the metrics used in table 1 and 2, both of which are standard. It is not directly clear how many runs per method/task combination are done e.g. where the variance in table 2 comes from, but this could possibly be reverse engineered from the implementation docs. The aggregation is also not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The authors provide an extensively documented method, with a clear introduction of the topic. They touch upon many subjects that are generally 'entry level' for AI before going in to the depth of the method, increasing accesibility. The complete documentation of the experiments, tasks, used methods and implementation significantly lower the requirement of previous knowledge or use of external materials to understand the method.
