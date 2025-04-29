
## Response Length Perception and  Sequence Scheduling: An LLM-Empowered LLM Inference Pipeline
Zangwei Zheng, Zangwei Zheng, Xiaozhe Ren, Fuzhao Xue, Yang Luo, Xin Jiang, Yang You
Keywords: 
NeurIPS/2023/Proceedings/70953 - Response Length Perception and  Sequence Scheduling: An LLM-Empowered LLM Inference Pipeline.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the subtitle (https://github.com/zhengzangw/Sequence-Scheduling). In the readme they state the method, give a few examples, installation requirements, how to prepare/collect the data, how to train, how to evaluate, and examples on how to to inference commands. The code can use more comments. The structure is easy. Overview is given in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide a dataset in their implementation including scripts and instructions on how to collect. THey discuss how it was collected in 4.2. using prompts from 2 other datasets with citations and description and statistics in appendix B. The resulting dataset has statistics in figure 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors use pretrained models and evaluate them. Then they conduct instruction tuning in 4.2. The hyperparameters are birefly summarised but amore structured overviw can be found in the implementation. No acquisition given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors define their own metric type (PiA and PO) which is measured in absolute error count and acc-50/acc-100 and failure percentage. In table 4 they present the respective improvement, tokens per batch and trhoughput per second from the models original answers and after training. Results are single model. No dataset split discussed.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on LLM and inference + sequence scheduling.
