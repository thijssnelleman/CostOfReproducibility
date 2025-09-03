## Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning
Jakub Grudzien Kuba, Ruiqing Chen, Muning Wen, Ying Wen, Fanglei Sun, Jun Wang, Yaodong Yang
Keywords: 
ICLR/2022/Proceedings/6244 - Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in a footnote on the first page (https://github.com/PKU-MARL/TRPO-PPO-in-MARL). In the readme they state installation instructions, how to use the environments, and where to find and run the training scripts. The code has decent comments. Structure is well organised.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use StarCraftII Multi-Agent Challenge (SMAC) and  Multi-Agent MuJoCo environments, provide citations and installation instructions in the implementation. The environments are described in section 5, although not in great detail.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The parameters are summarised in an extensive config.py script but not with seperate config files per experiment, although some values are present in their training scripts. The HP values per environment in appendix E, tables 1-7. Acquisition not given persay, although sometimes its stated that the values are 'most common'.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure average episode reward over environment steps but aggregation/variation is not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
