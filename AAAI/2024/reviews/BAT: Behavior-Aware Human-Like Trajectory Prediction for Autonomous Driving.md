
## BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous Driving
Haicheng Liao, Zhenning Li, Huanming Shen, Wenxuan Zeng, Dongping Liao, Guofa Li, Chengzhong Xu
Keywords: ROB: Motion and Path Planning, ROB: Other Foundations and Applications
AAAI/2024/Proceedings/29712 - BAT: Behavior-Aware Human-Like Trajectory Prediction for Autonomous Driving.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/Petrichor625/BATraj-Behavior-aware-Model). There is an extensive architecture illustration present in the paper and there are some notes on the implementation. On the readme of the implementation the authors state highlights, a notice that a code fix is available elsewhere, installation notes and requirements, data loading and preprocessing instructions, how to train the model and monitor it and where the resulting model can be found, and a statement that they are working on code for some visualizations. Finally they state their main contributions. The code has an easy structure to follow and has some comments in it. However, since it supposedly currently does not work, this could complicate things for re-implementation but should not make it impossible since they offer an alternative (their new project).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/4)

The authors state they use four data sets, which are public based on the citations titles, and provide citations on the first three (The fourth is introduced in this paper). Two of them have a preprocessor in the implementation docs. The authors state in the implementation that one data set would supposedly be available there at the 'releases', but is nowhere to be found. They give a brief description on it, but real statistics seem to be missing as well as details on how it was acquired. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

Soem details regarding the trajectories are given in the experimental set up, and an ablation study is done where they remove certain modules from their method. No other details are mentioned regarding configurations in the paper. These values seemingly can be extracted from the implementation but they are hard coded, and it is not actually stated that the values present there were actually used to produce the results.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state they use RSME as metric. They seem to be presenting single model evaluations in their experiment, based on the implementation details. It would have been better if this was clearly stated that for each result a single model is trained and evaluated once, as there is stochasticness in the training process. There are details provided regarding the division of the data into training and testing sets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires some epxertise regarding the subcategories, but it is in general well explained and the documentation regarding the implementation is well done, albeit non functional, this does guide the independent investigator a lot.
