
## Markov Chain Monte Carlo for Continuous-Time Switching Dynamical Systems
Lukas Köhs, Bastian Alt, Heinz Koeppl
Keywords: 
ICML/2022/Proceedings/18051 - Markov Chain Monte Carlo for Continuous-Time Switching Dynamical Systems.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://git.rwth-aachen.de/bcs/projects/lk/mcmc-ct-sds). In the readme they state installation instructions and an overview of the repository structure. The code is very well documented with comments. Pseudo code is available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/3)

The authors place a dataset in their implementation. They state they generated data in section 4. One generator is available in the code, the second and third are missing. In 3.2 and 3.3 the processes are explained. The parameter values are given in sec 4.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the HP values are set empirically. The values are discussed in appendix D. An informal overview is given in the appendix text (sort of a list) but it is difficult to match this to some code configuration file. The budget for empirical acquisition is not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method for 'Y' and 'pz' but these are not explicitly described as metrics, thus raising the expertise requirement for this experiment. No train/test split applicable. The variance is over the number of samples. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in markov chain and time series data.
