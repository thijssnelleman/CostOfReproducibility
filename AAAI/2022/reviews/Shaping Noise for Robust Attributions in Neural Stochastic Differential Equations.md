
## Shaping Noise for Robust Attributions in Neural Stochastic Differential Equations
Sumit Kumar Jha, Rickard Ewetz, Alvaro Velasquez, Arvind Ramanathan, Susmit Jha
Keywords: Philosophy And Ethics Of AI (PEAI)
AAAI/2022/Proceedings/21190 - Shaping Noise for Robust Attributions in Neural Stochastic Differential Equations.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state they use ResNet-50 in PyTorch. However not much other details are given in the paper. The authors provide a diagram on their method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The authors use the ImageNet benchmark data set, a publicly available data set. There are however no citations, statistics or direct links provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors state key hyperparameters for training the model, but it seems not all necessary values are given. This is could have been mitigated with implementation documentation. No details are provided on how the given values were determined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state how the training procedure was conducted, but no details regarding train or test splitting is presented, the reason for this could require a subfield expert to determine. The metrics for quantification are well explained. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The independent investigators need a wide range of expertise to understand the methed, specifically robustnuss. Furthermore, several details of the work are difficult to understand because of the complexity and combined with the missing implementation documentation the required expertise is subtantially exacerbated.
