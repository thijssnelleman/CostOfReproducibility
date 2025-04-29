
## Differentially Private Neural Tangent Kernels (DP-NTK) for Privacy-Preserving Data Generation
Yilin Yang, Kamil Adamczewski, Xiaoxiao Li, Danica J. Sutherland, Mijung Park
Keywords: 
JAIR/2024/Proceedings/15985 - Differentially Private Neural Tangent Kernels (DP-NTK) for Privacy-Preserving Data Generation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state a link to their implementation in section 5 (https://github.com/FreddieNeverLeft/DP-NTK). Code can use better comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(12/12)

The authors use MNIST, FashionMNIST, CelebA and CIFAR-10 and '8 benchmark tabular datasets' which are stated by name in table 4. The image datasets download automatically in the code. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter settings in appendix A and in the readmes of the implementation. The authors state these are 'Best Hyperparameters' in caption of table 5, but not how these were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the method with accuracy, 'performance' averaged over 5 independent runs, 'performance' as single run, and ROC/PRC/F1 score averaged over 5 independent runs. Data split not completely clear how applicable it is.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on data generation and privacy preservation.
