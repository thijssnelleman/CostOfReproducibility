
## Joint Human Pose Estimation and Instance Segmentation with PosePlusSeg
Niaz Ahmad, Jawad Khan, Jeremy Yuhyun Kim, Youngmoon Lee
Keywords: Computer Vision (CV), Machine Learning (ML), Intelligent Robotics (ROB), Humans And AI (HAI)
AAAI/2022/Proceedings/19880 - Joint Human Pose Estimation and Instance Segmentation with PosePlusSeg.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a source of their implementation (https://github.com/RaiseLab/PosePlusSeg). In the readme they provide a model architecture, how to set up the environment for their code, direct links to where to download the data and how the directory structure should be for the repository, how to run the train script, and a short note where to look for testing the model. They also present visualised results. The code itself has some comments but the file structure seems a bit convoluted and could do with some clarification.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use a public data set to evaluate the performance of their method. Direct download links and instructions are given in the implementation documentation. They cite the data set, but do not provide a lot of details/statistics on the data set itself.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in the experiments section. The full hyperparameters could be extracted from the implementation but this will take some effort. No specific details are given on how these are acquired, however the authors do an ablation analysis on some parameters later on.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors specify the train/test splitting of the data, and the types of experiments they conduct. There are no other details, and based on the results tables they seem single model results. This would need a bit of verification but should not be too difficult. The metrics are not clarified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method is on human pose / image segmentation tasks, and requires some understanding of the SOTA and the general metrics used. 
