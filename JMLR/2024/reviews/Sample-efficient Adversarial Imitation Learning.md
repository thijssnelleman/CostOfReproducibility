
## Sample-efficient Adversarial Imitation Learning
Dahuin Jung, Hyungyu Lee, Sungroh Yoon
Keywords: 
JMLR/2024/Proceedings/230314 - Sample-efficient Adversarial Imitation Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide implementation details in appendix B and cite the library they use for their simulators and that the implementation is based on PyTorch. Implementation is not shared. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors state and cite the libraries used for their environments in section 5 and appendix B. The authors use Ant-v2, HalfCheetah-v2, Walker2d-v2 in the main experiments. They are not described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters and their values are stated in appendix B. Acquisition not explained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the methods on the environments using 100 expert state-action pairs. In appendix B they state they reported the mean and standard error over 3 trials. Data split not applicable. Metric is environmental reward although this could have been stated a bit more clearly.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on RL and adversarial imitation learning.
