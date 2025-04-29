
## Self-Supervised Audio-and-Text Pre-training with Extremely Low-Resource Parallel Data
Yu Kang, Tianqiao Liu, Hang Li, Yang Hao, Wenbiao Ding
Keywords: Speech & Natural Language Processing (SNLP)
AAAI/2022/Proceedings/21334 - Self-Supervised Audio-and-Text Pre-training with Extremely Low-Resource Parallel Data.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors do not provide a source for their implementation. They cite two sources of which they use the original implementation and extend it, which they depict in figure 1a. They also provide pseudo code on the pre-training procedure. They also state how the original implementation is applied, and how they implement the loss functions for the text and audio. They also later state they reimplement a previous work of which they also follow the experimental protocol. Practical details on the implementation are not given, such as language, libraries etc. but could be inferred from sourced/cited work. This in general means there are some points to start to re-implement the method, however it will still be quite the effort.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use a data set which they cite and is seemingly publicly available for pretraining. They provide details on how the data set was used and a small description on it. They then use three  datasets to evaluate three tasks. They provide full details on how the data sets are used and a small description on the task. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors specify a short list of details regarding their hyperparameters in the pre-training details section. Its not specified how these were achieved and is unlikely to be the complete list of hyperparameters given the complexity of the method. An ablation study is done modular/data based on their method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the training procedures clearly and cite other works for the experiment protocol. For the first task they state they use 5-fold cross-validation as procedure, for the second and third this would have to be verified by reading the citations. The main effort indicated here is having to check with the citations which evaluation method was exactly used per data set / task. The metrics are clearly stated for each task.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method requires a good understanding of NLP, deep learning, pretraining and state of the art LLMs.
