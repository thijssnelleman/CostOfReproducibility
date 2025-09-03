## Open-vocabulary Object Detection via Vision and Language Knowledge Distillation
Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, Yin Cui
Keywords: 
ICLR/2022/Proceedings/6372 - Open-vocabulary Object Detection via Vision and Language Knowledge Distillation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/vild). The readme contains an intro to the method, a link to a demo notebook, installation requirements, links to the datasets and how to place them in the repository, how to preprocess the data, link to model checkpoints and their respective configurations, how to download a second dataset and how to run inference on it, and acknowledgements for other repos used to built this one. The repository is well structured and has a lot of comments. Overview given in figure 2. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use LVIS and COCO, providing citations and descriptions. For LVIS a download link is provided in the readme of the implementation. They furthermore use PASCAL VOC 2007 and Objects365 for evaluation but provide little detail on these.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide two configuration files in the implementation, and link which trained model was produced with which in the readme (very nice). They list a few values in text in sec 4, and details about hyperparameter sweeps in appendix C, as well as appendix D.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use the provided dataset splits and state in each table which is used. They measure AP and average over 3 runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
