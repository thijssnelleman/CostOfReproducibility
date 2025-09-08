## Distributed Differential Privacy in Multi-Armed Bandits
Sayak Ray Chowdhury, Xingyu Zhou
Keywords: 
ICLR/2023/Proceedings/11384 - Distributed Differential Privacy in Multi-Armed Bandits.pdf
Project URL: https://openreview.net/attachment?id=cw8FeirkIfU&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link in the abstract (https://github.com/IST-DASLab/CrAM). In the readme they provide an overview of the files, how to run the code with example parameter values, where to find model checkpoints with details on the model, installation requirements, and acknowledgements for inspiration code. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use CIFAR-10 (Citation),  SQuADv1.1 (Citation) and ImagNet. No direct links or details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The repository contains five configuration files with training details per model, appendix B and C provide further details, and for a few HPs the authors provide a motivation but not for all.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors use the static train/test splits from the datasets, measure test accuracy and validation f1 score, relative error increase, aggregation and variation now always clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
