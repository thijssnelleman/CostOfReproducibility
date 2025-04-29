
## Spear: Evaluate the Adversarial Robustness of Compressed Neural Models
Chong Yu, Tao Chen, Zhongxue Gan, Jiayuan Fan
Keywords: Computer Vision: CV: Adversarial learning, adversarial attack and defense methods, Machine Learning: ML: Adversarial machine learning, Machine Learning: ML: Robustness
IJCAI/2024/Proceedings/0177 - Spear: Evaluate the Adversarial Robustness of Compressed Neural Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors state the framework used to implement 'all algorithms', and cite it / provide a direct link. They also state a few libraries used for certain parts of the implementation, with more details in 4.2. Figure 3 has a detailed workflow of the method, figure 2 a more high level difference. The authors do not share their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors state the target models used in 4.2 and provide citations + direct links. The authors state several data sets with citation in 4.3 from which they use the test sets. Not many other details are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The parameter values are stated per experiment, and in table 1 a grid of evaluations is shown. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in 4.3. The details of each attack are summarised in table 1. The authors state they conduct some training on ImageNet in section 4.5, but a lot of details require some expertise on adverserial attacks and robustness to determine.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The work requires (pratical) previous experience with robustness and adversarial attacks to grasp the exerpiments conducted and reproduce the implementation.
