
## Expression might be enough: representing pressure and demand for reinforcement learning based traffic signal control
Liang Zhang, Qiang Wu, Jun Shen, Linyuan Lü, Bo Du, Jianqing Wu
Keywords: 
ICML/2022/Proceedings/16173 - Expression might be enough: representing pressure and demand for reinforcement learning based traffic signal control.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (The href leads to github: LiangZhang1996/Advancd_XLight) but it gives a 404. This seems to be due to a typo ('advancd' is mispelled) and with the correction can easily be confirmed to match the paper (https://github.com/LiangZhang1996/Advanced_XLight). The readme states how to cite the paer and installation requirements, how to run the code, details and links to baselines, overview on the code files. The code has very few comments. In figure 1 they illustrate the task, in algorithm 1 and 2 pseudo code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors state they use 3 real world traffic datasets (One consists of three subsets) for which they provide a link and explain in 5.2. They also use a simulator which they explain and provide a direct link to. The simulator parameters are stated in 5.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method takes weights as a parameter. In 4.1.2 the authors state they 'test several simple weights and find the best as final results of this method'. This is analysed in 5.5.1. in figure 2. The actio nduration parameter is analysed in figure 3.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure average travel time in seconds (task specific). This is explained in 5.3. The results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise in RL and traffic tasks/simulators especially since the implementation is missing practical expertise is needed.
