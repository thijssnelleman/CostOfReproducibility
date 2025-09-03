## Learning Long-Term Reward Redistribution via Randomized Return Decomposition
Zhizhou Ren, Ruihan Guo, Yuan Zhou, Jian Peng
Keywords: 
ICLR/2022/Proceedings/6587 - Learning Long-Term Reward Redistribution via Randomized Return Decomposition.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in 4.1 in footnote 1 (https://github.com/Stilwell-Git/Randomized-Return-Decomposition). In the readme they state installation requirements, how to run the commands with the parameter values to reproduce the main results for their paper. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors use simulated environments (Ant-v2, HalfCheetah-v2, Walker2d-v2, Humanoid-v2, Reacher-v2, Swimmer-v2, Hopper-v2 and HumanoidStandup-v2) from MuJoCo in OpenAI Gym and provide a citation. The parameters of the simulation are specified in 4.1. and the installation is specified in the implementation. Details on the tasks are not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors list the hyper-parameter configuration in table 1 and 2 of appendix B. They also vary the value of parameter K over a grid in figure 2. The other values are based on previous works which are cited.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure learning curves over timesteps with 30 random initialised runs, presenting the standard deviation. They also smooth the curves using the average over 10 most recent evaluation points. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
