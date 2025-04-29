
## FlexiBO: A Decoupled Cost-Aware Multi-Objective Optimization Approach for Deep Neural Networks
Md Shahriar Iqbal, Jianhai Su, Lars Kotthoff, Pooyan Jamshidi
Keywords: 
JAIR/2023/Proceedings/14139 - FlexiBO: A Decoupled Cost-Aware Multi-Objective Optimization Approach for Deep Neural Networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in section 1.1 (https://github.com/softsys4ai/FlexiBO). In the readme they state dependencies that need to be resolved but no versions, links to reviews of the paper and how to run the code. Code has good comments. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors use ImageNet, MNISt, CIFAR-10, SQuAD 2.0, IMDB Sentiment and Common Voice datasets in their experiments. They are described and cited in 6.1.2 and the data can also be found in the implementation. There are some high level meta statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the architecture per experiment/dataset in table 2. This can also be found in the code. The hyperparameters of the surrogate models are given in table 6. The authors measure prediction error and energy consumption of 20 randomly selected designs from a design space and take 10 repeated measurements and consider the mean (for energy). The design space is defined in a yaml file in the implementation. As the authors actually evaluate the HPO method, the selected values are less important. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The training/test set sizes are stated in table 2. The authors measure hypervolume error (6.1) and number of evaluations as well as the log of the wallclock time. The presented variance is not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on MO HPO.
