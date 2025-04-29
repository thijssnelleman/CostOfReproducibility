
## Stop-Gradient Softmax Loss for Deep Metric Learning
Lu Yang, Peng Wang, Yanning Zhang
Keywords: CV: Image and Video Retrieval, CV: Learning & Optimization for CV, CV: Representation Learning for Vision
AAAI/2023/Proceedings/25421 - Stop-Gradient Softmax Loss for Deep Metric Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state implementation details in the paper, with which library their implementation was made. The authors provide a small architecture schematic. No implementation source is given, and with the few details specified it makes it a huge effort to re-implement the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use four public benchmark data sets for their experiments. They provide citations on them, a small description and some key statistics but. Finding these data sets should be little effort but no direct links are given. Details are given how the data was reformatted for their implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors use Resnet with the same settings as the original work. As the authors provide a loss method, with some hyperparameter defintions and explore some of these values with exhaustive grid search.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state their evaluation protocol briefly and note it is in line with other works. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires some understanding of loss functions, but is generally quite accessible. It could be improved by providing the implementation, such that independent investigators have examples to work with.
