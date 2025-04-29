
## DySLIM: Dynamics Stable Learning by Invariant Measure for Chaotic Systems
Yair Schiff, Zhong Yi Wan, Jeffrey Parker, Stephan Hoyer, Volodymyr Kuleshov, Fei Sha, Leonardo Zepeda-Nunez
Keywords: 
ICML/2024/Proceedings/35055 - DySLIM: Dynamics Stable Learning by Invariant Measure for Chaotic Systems.pdf
Project URL: https://github.com/google-research/swirl-dynamics/tree/main/swirl_dynamics/projects/ergodic

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a project URL on the ICML website and link it in their paper as implementation code as well (https://github.com/google-research/swirl-dynamics/tree/main/swirl_dynamics/projects/ergodic). In the readme the authors state an introduction to the work, link a demo on how the experiments can be run, explain where to find the configuration files, how to run the main etnry point, how the data can be acquired and used with their code. The code has a lot of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/3)

The authors state two data sets on the implementation, on is generated on the fly the other they provide a download link for. They details the generator in appendix E.1 and cite a source for it. In section 5.2 they discuss the downloadable setting. The third system is described in 5.3, but this is seemingly not available in the implementation. It is described just as extensively as the other systems.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The configurations used per experiment are fully specified in seperate files in the implementation docs. There a few remarks on optimisation, but a full acquisition strategy is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state all experiments were repeated five times with random seeds. It is not clear how these are aggregated. The authors detail the experiment metrics in sec 5 and describe them fully in appendix C. There are also some mentions of test sets in the appendix but this is not fully clarified. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on regularisation and learning dynamics.
