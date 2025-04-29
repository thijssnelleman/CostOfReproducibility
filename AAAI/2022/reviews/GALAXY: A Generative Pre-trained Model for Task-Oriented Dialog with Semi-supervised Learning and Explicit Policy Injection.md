
## GALAXY: A Generative Pre-trained Model for Task-Oriented Dialog with Semi-supervised Learning and Explicit Policy Injection
Wanwei He, Yinpei Dai, Yinhe Zheng, Yuchuan Wu, Zheng Cao, Dermot Liu, Peng Jiang, Min Yang, Fei Huang, Luo Si, Jian Sun, Yongbin Li
Keywords: Speech & Natural Language Processing (SNLP)
AAAI/2022/Proceedings/21320 - GALAXY: A Generative Pre-trained Model for Task-Oriented Dialog with Semi-supervised Learning and Explicit Policy Injection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/siat-nlp/GALAXY). In the readme the authors provide some excerpts from the paper, installation requirements, where to download the data and how to set it up for the code, details regarding pretraining, how to run the training scripts, how to run the inference scripts and some references to what they based their code on. The code has a decent amount of comments. The configurations per run are noted in the .sh scripts. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two 'well studied' benchmark data sets and provide citations on them. They provide descriptions on them and how many smaples will go into t/v/t split. Direct download link available in repository. A few more statistics on  the data would have been welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The exact configurations used for each run can be found in the implementation documentation, with a bit of effort. No notes about it are made however in the paper, so we know nothing about how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics they use for evaluation and provide citations on them. A short description is given on the experiment, the train/test procedure is clear and more details can be inferred from the implementation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires some understanding of the task, although good examples are provided. Also requires a good understanding of NLP.
