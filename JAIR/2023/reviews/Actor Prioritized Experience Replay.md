
## Actor Prioritized Experience Replay
Baturay Saglam, Furkan B. Mutlu, Dogan C. Cicek, Suleyman S. Kozat
Keywords: 
JAIR/2023/Proceedings/14819 - Actor Prioritized Experience Replay.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the introduction, footnote 1 (https://github.com/baturaysaglam/LA3P). The authors describe the method and which repositories they build upon, where to find the results, under which dependencies the results were produced, how to use the code with argument descriptions. Code has okay comments, structure is straightforward.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use simulated environments Ant, HalfCheetah, Humanoid, Walkerd2d from OpenAI Gym and MuJoCo (included in env installation). The environments are not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter settings are described in appendix B. The values are summarised per model in table 7. They state the delta parameter was selected from a grid, but also state no HPO was done except for SAC.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Results are presented with average and 95% CI with asliding window of size 5. In table 1/4 they present average return and 95% CI. Metrics are evaluation reward (environment based).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in RL.
