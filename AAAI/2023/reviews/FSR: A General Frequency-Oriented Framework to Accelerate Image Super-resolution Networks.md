
## FSR: A General Frequency-Oriented Framework to Accelerate Image Super-resolution Networks
Jinmin Li, Tao Dai, Mingyan Zhu, Bin Chen, Zhi Wang, Shu-Tao Xia
Keywords: CV: Low Level & Physics-Based Vision, CV: Applications, CV: Computational Photography, Image & Video Synthesis
AAAI/2023/Proceedings/25218 - FSR: A General Frequency-Oriented Framework to Accelerate Image Super-resolution Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/THU-Kingmin/FSR). They give a figure in the readme on their methods results, the general framework, a description of dependencies, some source the code was based on, a data set statement, and how to train and test the method. The code has some comments but could do with some more. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors state they use 4 publicly available data sets from existing literature. They motivate their data set selection in the experiments section. They also state in their training section a different training data set is used which is not mentioned in the implementation docs. Citations on the data sets are provided. General statistics are missing. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state their hyperparameter values in the training details section. Default values can be found in the implementation. No details are given on how these values were acquired. The authors do a modular ablation study.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The metrics used are not introduced. The authors provide single model results. The training and testing suite is clearly stated. The authors provide visual results of the experiment (example output).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of super-resolution image networks.
