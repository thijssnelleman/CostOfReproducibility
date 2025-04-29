
## Opponent-Limited Online Search for Imperfect Information Games
Weiming Liu, Haobo Fu, Qiang Fu, Wei Yang
Keywords: 
ICML/2023/Proceedings/25196 - Opponent-Limited Online Search for Imperfect Information Games.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide an implementation for their experiments. The authors refer a framework for reinforcement learning in games. No other details can be found.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/2)

The authors simulate two games: Poker and Mahjong. The games are described in great details in appendix B and the parameters specified in section 7. Implementations are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the hyperparameter values in appendix D, with some of them evaluated over a range. They state the best (found) value in a seperate column. The cofnigurations were evaluated against eachother in the games.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method on the simulator over iterations (no split applicable) and measure 'exploitability' defined is section 2. Values are single run in table 2 and figure 4/5. In table 3 the variance is CI 95% and the population is the various configurations. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in RL and game theory.
