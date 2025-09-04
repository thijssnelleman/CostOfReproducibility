## Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching
Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong
Keywords: 
Award: Outstanding Paper Award
ICLR/2023/Proceedings/1136 - Universal Few-shot Learning of Dense Prediction Tasks with Visual Token Matching.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/GitGyun/visual_token_matching). In the readme they give an overview on the method, how to download the datasets and how to store in in their code, how to modify the settings according to your system, how to install requirements, and where to find model checkpoints to use including which one they used for their experiment. Training, finetuning and evaluation scripts usage with example parameter values are given and how to finally get the output results. Furthermore they list several repositories used to build theirs. The code could use more comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use the Taskonomy dataset, describe the usage in 5.1. and more information in appendix A including citations. Download instructions in the implementation and includes the scripts used for the described modification.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors provide three labelled configuration files in their repository. Details are given in appendix B.3. Values are not motivated.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure mIoU, mErr, RMSE over a five fold split and present the metrics per fold. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
