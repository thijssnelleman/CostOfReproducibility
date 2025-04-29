
## Towards Theoretical Analysis of Transformation Complexity of ReLU DNNs
Jie Ren, Mingjie Li, Meng Zhou, Shih-Han Chan, Quanshi Zhang
Keywords: 
ICML/2022/Proceedings/16187 - Towards Theoretical Analysis of Transformation Complexity of ReLU DNNs.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/sjtu-XAI-lab/transformation-complexity). The readme contains installation notes, how to run the code with two examples and links to demos for the experiments of the paper. The code has few comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

There are automatic data downloaders in the implementation for CIFAR10 and MNIST. Citations are provided in section 4, paragraph experimental settings. For the other datasets (CelebA, Pascal VOC and Tiny ImageNet) downloaders/links are not provided. The data is not described in the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss a hyperparameter in appendix G.2. and its values. In figure 10 they experiment with different values. Based on the analysis they set the value. The model architectures are defined in experimental settings (but are not persay parameters of the method itself).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state in G.1. that they randomly sample 2k from training for the transformation complexity calc. The metrics are defined in section 3. There are mention of test metric values but no mention of train/test splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on transformation complexity and activation functions in DNNs.
