
## VeXKD: The Versatile Integration of Cross-Modal Fusion and Knowledge Distillation for 3D Perception
JI Yuzhe, Yijie CHEN, Liuqing Yang, Ding Rui, Meng Yang, Xinhu Zheng
Keywords: 
NeurIPS/2024/Proceedings/95130 - VeXKD: The Versatile Integration of Cross-Modal Fusion and Knowledge Distillation for 3D Perception.pdf
Project URL: https://papers.nips.cc/paper_files/paper/2024/file/e34d908241aef40440e61d2a27715424-Supplemental-Conference.zip

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide supplementary material (https://papers.nips.cc/paper_files/paper/2024/file/e34d908241aef40440e61d2a27715424-Supplemental-Conference.zip) with their code in it. In the readme they state an overview of the method, installation requirements, a detailed structure of the repository, how to run the code regarding data creation, evaluation and training. They also give an overview what are the key files of implementation they did in this work. Finally they link the repositories they used for their implementations. The files they mention they contributed have good comments. However, even though the repo has an index, the structure is still massive and a lot of the code is not theirs so its difficult to say what they did and did not influence to guide you through it to understand what is relevant.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state the dataset used in 4.1. with a citation with a description and some statistics. There could be a bit more information. A direct link is given in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the models and methods used in their framework in 4.1. In appendix B the authors state the values per experiment. Acquisition is not specifed. There are a lot of configuration files in the implementation but its not clear which belong to the presented method, so the overview is only informally stated in the text.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the data split and metrics are given in 4.1., which are provided by the data set source (metrics are standard). The second task is provided by a previous work and the metric is standard and defined over the data. The results are seemingly single model but this is not explicitly stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on CV and 3D perception.
