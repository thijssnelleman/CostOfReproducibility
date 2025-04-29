
## Explainable Multi-Agent Reinforcement Learning for Temporal Queries
Kayla Boggess, Sarit Kraus, Lu Feng
Keywords: Agent-based and Multi-agent Systems: MAS: Human-agent interaction
IJCAI/2023/Proceedings/0007 - Explainable Multi-Agent Reinforcement Learning for Temporal Queries.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/kjboggess/ijcai23). In the readme they state installation details, how to download the environments used, how to train a policy, how to evaluate, and how to generate output files/analysis. The repository is quite large but well structured. It has quite some comments in the code, however there seems to be a lot of duplicate/copied code in the repository. In general the documentation could do with an index on the structure. The authors state pseudo code in their paper on the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors state they apply their method to four benchmarks. They provide direct links to these in their implementation docs. The authors provide a short description and citations on each environment.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

A few parameter values are stated in section 5. It is not directly clear if all needed hyperparameters are given, as there is no summary and the implementation is difficult to analyse what is needed.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The numerical experiments require some domain knowledge to understand, but the set up is well documented (table 1) parameterwise. The authors also do a user study (figure 3 show the questionaire) which is explained in 6.1 and the population of participants as well.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in RL.
