
## DiffStitch: Boosting Offline Reinforcement Learning with Diffusion-based Trajectory Stitching
Guanghe Li, Yixiang Shan, Zhengbang Zhu, Ting Long, Weinan Zhang
Keywords: 
ICML/2024/Proceedings/33032 - DiffStitch: Boosting Offline Reinforcement Learning with Diffusion-based Trajectory Stitching.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/guangheli12/DiffStitch). In the readme they state examples on how to run the code and something regarding bugs. There is an environment file regarding the installation. The code has a decent amount of comments. The repository structure could use an explanation. The readme could be better. There is an overview on their method in figure 2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use benchmark environments to evaluate their method, which they cite and describe in 5.1. They are included in the implementation. Their specific adaptations are present there as well. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify the hyperparameters in appendix A, a full list per experiment can be found in the implementation. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the result averaged normalized score with the standard deviation. The metric is based on the environment. The experiment is repeated three times with random seeds. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on RL.
