
## Learning Iterative Reasoning through Energy Minimization
Yilun Du, Shuang Li, Josh Tenenbaum, Igor Mordatch
Keywords: 
ICML/2022/Proceedings/17507 - Learning Iterative Reasoning through Energy Minimization.pdf
Project URL: https://energy-based-model.github.io/iterative-reasoning-as-energy-minimization/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a project URL from which they link the implementation (https://github.com/yilundu/irem_code_release). In the readme they give an overview of the method, installation instructions, various examples on how to run the code with different parameters. The code has a decent amount of comments. The structure is small and easy to oversee. Pseudo cdoe is given in algorithm 1/2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use data generators for their method. The generators are available in their implementation. The parameters and descriptions are given per experiment in section 4.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The possible parameters for the code are summarised in the implementation files 'graph_train.py' and 'train.py' arguments. The authors state training parameters in appendix C which are specified per data set. The architectures are given in table 6-13. No acquisition or search specified for the selected settings.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use Mean Squared error as metric. The results are single model. Test set not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in AI reasoning and energy minimsation. 
