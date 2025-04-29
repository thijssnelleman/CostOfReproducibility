
## Hyena Hierarchy: Towards Larger Convolutional Language Models
Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, Christopher Re
Keywords: 
ICML/2023/Proceedings/1735 - Hyena Hierarchy: Towards Larger Convolutional Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in appendix A (https://github.com/HazyResearch/safari). Here not the entire repository is dedicated to the method but the method is part of the repository. In src/models/sequence we find the file dedicated. The file is rich in comments. Furthermore there is a standalone file in the main directory which is a simplified version of the former, which is also well documented with comments. There is a requirements file in the repository. An overview of the method is available in figure 1. Algorithm 1-3 give pseudo code on the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use two datasets for training, WikiText103 and the pile. On one a citation is provided. Direct links, statistics and descriptions not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the hyperparameters and their settings in table 4 and 6 of the appendix. There are also config files available in the implementation but it would have to be verified which are relevant to the experiments. They derive these values from previous works ('standard GPT hyperparameters') after some preliminary experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the models for perplexity, FLOPs, Test accuracy, associative recall and loss. Data split is train/test but how is not specified. results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on large convolutional models.
