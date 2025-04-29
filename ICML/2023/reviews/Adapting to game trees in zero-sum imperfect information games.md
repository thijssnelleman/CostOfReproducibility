
## Adapting to game trees in zero-sum imperfect information games
Côme Fiegel, Pierre Menard, Tadashi Kozuno, Remi Munos, Vianney Perchet, Michal Valko
Keywords: 
Award: Outstanding Paper
ICML/2023/Proceedings/1488 - Adapting to game trees in zero-sum imperfect information games.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their code in section 6 (https://github.com/anon17893/IIG-tree-adaptation). There they state how to run the experiments and how to produce plots. There is an installation file present. The comments are good and the structure is simple. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors simulate games and state them with citations and from which library they use the implementation from. Descriptions are a bit lacking per game. Parameter values are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors summarise the experiment configuration in a file and seperate files per agent for their configurations. The authors provide a description on it in sec 6 stating they conducted grid search for each agent/game combination but not what these grids were.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors use exploitability as a metric (formula given in fig 1. caption) over epsiodes. The population, aggregation and variation is not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise in imperfect information games and game trees.
