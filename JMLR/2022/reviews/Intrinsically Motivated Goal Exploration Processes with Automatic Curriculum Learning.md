
## Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning
Sébastien Forestier, Rémy Portelas, Yoan Mollard, Pierre-Yves Oudeyer
Keywords: 
JMLR/2022/Proceedings/210808 - Intrinsically Motivated Goal Exploration Processes with Automatic Curriculum Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote one of section 4.1 (https://github.com/sebastien-forestier/IMGEP). The readme is empty. Code has okay comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/3)

The authors create three environments in 4.1. and describe them in detail. Only the 2D simulation is provided in the code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors specify their method in algorithm 1. They are also defined in 'run.py' of their implementation. There are some notes about their values in section 4 but the re is no clear summary or acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method on each environment averaged over 11 runs and show results over parts of the environment (stepping-stones) in figure 8 and measure moving %. In table 2 they show the 'competence' of 25 50 and 75 percentiles. Figure 10 shows the instrinsic reward (algorithmic metric) per environment. Some metrics are not completely clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on curriculum learning.
