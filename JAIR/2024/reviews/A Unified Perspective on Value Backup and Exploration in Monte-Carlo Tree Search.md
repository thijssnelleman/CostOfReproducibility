
## A Unified Perspective on Value Backup and Exploration in Monte-Carlo Tree Search
Tuan Dam, Carlo D'Eramo, Jan Peters, Joni Pajarinen
Keywords: 
JAIR/2024/Proceedings/16019 - A Unified Perspective on Value Backup and Exploration in Monte-Carlo Tree Search.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 2 (https://github.com/damquangtuan/UnifiedMCTS). There is a readme in three of the sub directories, with installation requirements. The code has okay comments. A general index on the repository would be welcome as well.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors use four simulated environments, followed by a benchmark environment and state from which library they use them. They are described in 7.1, 7.2 and 7.3. They are included in the repository installation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors conduct a hyperparameter search and state the values in appendix D table 6 for the benchmark. They conduct grid search for optimisation, and specify the grids per experiment and which value was selected. Some parameters have fixed values but how these are fixed to these values is not explained. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results as mean + 2 std dev over the success rate over 100/500 evaluations. They also measure discounted reward (env metric) with mean + standard error over 100/1000 runs. Data split not applicable. In table 5 they present the average score (environemnt based) over 100 seeds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on MCTS.
