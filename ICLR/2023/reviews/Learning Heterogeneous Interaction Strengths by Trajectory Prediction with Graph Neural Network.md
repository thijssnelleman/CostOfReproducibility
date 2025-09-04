## Learning Heterogeneous Interaction Strengths by Trajectory Prediction with Graph Neural Network
Seungwoong Ha, Hawoong Jeong
Keywords: 
ICLR/2023/Proceedings/11860 - Learning Heterogeneous Interaction Strengths by Trajectory Prediction with Graph Neural Network.pdf
Project URL: https://openreview.net/attachment?id=qU6NIcpaSi-&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in section 4 (https://github.com/nokpil/RAIN). In the readme they state installation requirements, how to run experiments, how to generate datasets with example instructions and parameter values. Code has ok comments and several directories have extra readmes with further explanations.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

In 4.1 the authors use two simulators which they describe, and provide code for in the implementation. In 4.2 the authors use CMU motion database, cite it and describe it briefly, it downloads automatically in the code. Statistics etc are a bit lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors mention hyperparameter values and architecture details in text in the supplementary materials. Structured overview is missing and no motivation for value selection found.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure MSE, and state the data split in 4.1. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
