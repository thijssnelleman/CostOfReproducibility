
## A High-Resolution Dataset for Instance Detection with Multi-View Object Capture
QIANQIAN SHEN, Yunhan Zhao, Nahyun Kwon, Jeeeun Kim, Yanan Li, Shu Kong
Keywords: 
NeurIPS/2023/Proceedings/73409 - A High-Resolution Dataset for Instance Detection with Multi-View Object Capture.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors link their implementation in the subtitle (https://github.com/insdet/instance-detection). In the readme they state the dataset with links, a descriptions on the data, acknowledgemetns their project build upon and a description of a demo. The code can use more documentation. Installation notes are given in the supplementary material. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors create a new dataset in this work. The authors motivate the task, and describe the protocol for construction in section 3. The dataset is described in detail in 3.2. statistics are available in fig 3/4 and table 2. The dataset is linked in their implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors benchmark various methods on their new dataset and state a few HPs with values in section 5. A full overview is missing. Acquisition not as relevant as they are benchmarking other methods on their new dataset. Overview is not given and it does not seem all parameters are presented.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors benchmark baselines on the new dataset. They state they synthesise a training and validation set and the process is described in sec 5. The metrics are explained in 5.1. The results are single model. It is implied that the results are on the validation set but not explicitly stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on instance detection in CV.
