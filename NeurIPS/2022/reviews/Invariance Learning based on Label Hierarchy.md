
## Invariance Learning based on Label Hierarchy
Shoji Toyota, Kenji Fukumizu
Keywords: 
NeurIPS/2022/Proceedings/53728 - Invariance Learning based on Label Hierarchy.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation in the supplementary materials (https://openreview.net/attachment?id=Y6xuQZP7t3&name=supplementary_material). There are no installation instructions. The code structure is easy to oversee (directory with code per experiment). Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use Colored MNIST and ImageNet as dataset. No links given. Citations present. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors use various configurations over a grid which they state for both experiments and select the best after delta_after epochs. A structured overview of the HPs is not given (only written in text). The selected HPs are not stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate test accuracy + std error over 5/10 runs. They use a test set for both experiments. They employ two strategies for splitting the data, Tr-CV and LOD-CV. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on invariance learning.
