
## Improving Policy Optimization with Generalist-Specialist Learning
Zhiwei Jia, Xuanlin Li, Zhan Ling, Shuang Liu, Yiran Wu, Hao Su
Keywords: 
ICML/2022/Proceedings/18319 - Improving Policy Optimization with Generalist-Specialist Learning.pdf
Project URL: https://zjia.eng.ucsd.edu/gsl

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/SeanJia/GSL). In the readme they introduce the method with pseudo code and extensive explanations on code snippits. They also refer to a tutorial script. The code is well documented and the repository is small. No installation files/explanations.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors illustrate the environments in figure 3. They note the benchmarks used for the experiments with citation in 5.4 and explain them extensively. The authors refer to the public libraries used for implementation of these environments in their implementation docs.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the hyperparameter values in appendix A per environment / method. Their own hyper-parameter (plateau criteria H) 'require some hyper-parameter tuning' which they discuss in an ablation study and appendix B. Full clarity on hyper-parameter tuning is not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method over raw episode rewards and report average with standard deviation over 5 or 3 runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise in DRL and generalists/specialist agents.
