
## Scaling Laws from the Data Manifold Dimension
Utkarsh Sharma, Jared Kaplan
Keywords: 
JMLR/2022/Proceedings/201111 - Scaling Laws from the Data Manifold Dimension.pdf
Project URL: https://github.com/U-Sharma/NeuralScaleID

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website and in footnote 6 (https://github.com/U-Sharma/NeuralScaleID). In the readme they index several files, describe how to use the code for both training and evaluation. There is an installation requirements file ('dependencies.yml'). Code can user better comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The author use in 3.2 CIFAR10, MNIST and SVHN: All download automatically in the code and citations are provided but no other details. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The neural network configurations can easily be extracted from the code (architecture, hyperparmeter values) due to their structure. The authors experiment is focussed on scaling down architectures (which they do on a grid). Their main parameters regarding the teacher network are d and k, which are varied in the experiments for analysis.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate loss and error (formula given) and report both train and test curves. The data split is (based on the code) a static split per dataset. Each dot on the figures 6/7 is a run. For figure 8/9 they present Loss and test loss over various network sizes but variances are not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on scaling laws for model sizes/capacity.
