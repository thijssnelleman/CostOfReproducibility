## CrAM: A Compression-Aware Minimizer
Alexandra Peste, Adrian Vladu, Eldar Kurtic, Christoph H Lampert, Dan Alistarh
Keywords: 
ICLR/2023/Proceedings/11058 - CrAM: A Compression-Aware Minimizer.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

Authors provide a link to their implementation in the abstract (https://github.com/IST-DASLab/CrAM). Readme has a structure overview, where to find example scripts on how to run, actual example code, where to find model checkpoints, installation requirements, and acknowledgements. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

Authors use ImageNet,  SQuADv1.1,  CIFAR-10, citations provided no descriptions. Downloads through code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

Hyperparameters detailed in text in appendix B. Config files available per experiment in implementation. Acquisition not specified for all.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

They measure validation accuracy averaged over 10 trials as wel as error increase with 70% CI. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
