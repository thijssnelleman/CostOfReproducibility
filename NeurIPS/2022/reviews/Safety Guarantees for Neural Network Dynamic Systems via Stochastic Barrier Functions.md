
## Safety Guarantees for Neural Network Dynamic Systems via Stochastic Barrier Functions
Rayan Mazouz, Karan Muvvala, Akash Ratheesh Babu, Luca Laurenti, Morteza Lahijanian
Keywords: 
NeurIPS/2022/Proceedings/52992 - Safety Guarantees for Neural Network Dynamic Systems via Stochastic Barrier Functions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their code in reference 43 (https://github.com/aria-systems-group/NeuralNetControlBarrier) but they also provide it as supplementary material. In the readme they state the purpose of the code, how to install to repeat the experiments, how to run, how to configure. The code has good comments. The structure is complicated and needs an index. Pseudo code in 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use 4 simulated environment for their experiments (Husky 4D and 5D are the same). For this they used the OpenAI gym environment which they cite but its not clear if it automatically installs in the code. Environment parameters given in table 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Architecture values are stated in table 1 per experiment. The authors refer for more details on the hyperparameters to appendix A but this is not given in the NeurIPS/openreview version. The authors evaluate various architectures in their experiment as acquisition (grid).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate Beta, P, time in minutes on the models. Train test split not applicable. Results are single model. Metrics are not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on NN dynamical systems moddeling.
