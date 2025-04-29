
## HEBO: Pushing The Limits of Sample-Efficient Hyper-parameter Optimisation
Alexander I. Cowen-Rivers, Wenlong Lyu, Rasul Tutunov, Zhi Wang, Antoine Grosnit, Ryan Rhys Griffiths, Alexandre Max Maraval, Hao Jianye, Jun Wang, Jan Peters, Haitham Bou-Ammar
Keywords: 
JAIR/2022/Proceedings/13643 - HEBO: Pushing The Limits of Sample-Efficient Hyper-parameter Optimisation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors prsent thier implementation in the introduction, footnote 1 (https://github.com/huawei-noah/HEBO). In the readme they overview a lot of methods, present results and abstracts/links to papers. The repository contains alot of different projects, each containing their own readmes and docs, and the comments are in general quite fine. Each has its own installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors use six real world UCI datasets and state them in 5.1. with citation but no other details are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors tune hyper-parameters of other methods in this work. They define the parameters and their domains in table 2 and 3. The process is described in detail in section 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors repeat each run with 20 random seeds and report normalised score as defined in eq. 3. They are reported with mean, std, median, and xth centiles. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on HPO.
