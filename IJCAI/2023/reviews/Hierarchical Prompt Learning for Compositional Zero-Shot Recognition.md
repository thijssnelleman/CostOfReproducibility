
## Hierarchical Prompt Learning for Compositional Zero-Shot Recognition
Henan Wang, Muli Yang, Kun Wei, Cheng Deng
Keywords: Computer Vision: CV: Recognition (object detection, categorization), Computer Vision: CV: Transfer, low-shot, semi- and un- supervised learning
IJCAI/2023/Proceedings/0163 - Hierarchical Prompt Learning for Compositional Zero-Shot Recognition.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state some implementation details at the end of section 4.1., that their model is implemented with pytorch and that they follow certain previous work for it. Figure 2 gives an overview. No other details specified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

In 4.1 the authors state the datasets used, three benchmark datasets for which the present a citation, a description on each and details numerical information in table 1. No direct link available to the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state their hyperparameter values per data set in the implementation details. It is difficult to verify if all needed values are there without a summary/implementation/pseudo code. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The auhtors state the evaluation metrics in 4.1 with an explanation and some citations. They state for the data they us 'standard split in previous work' and cite a source. They detail this numerically in table 1. The results seem to be single run/model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires experience with zero shot learning and CV. The lack of implementation means a lot of practical experience is required to re-implement the presented method.
