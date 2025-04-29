
## Adversarial Robustness against Multiple and Single $l_p$-Threat Models via Quick Fine-Tuning of Robust Classifiers
Francesco Croce, Matthias Hein
Keywords: 
ICML/2022/Proceedings/16203 - Adversarial Robustness against Multiple and Single l_p-Threat Models via Quick Fine-Tuning of Robust Classifiers.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/fra31/robust-finetuning). In the readme they describe their method, index the cdoe files with argument explanation, download links to pretrained models, how to evaluate and credits to other repositories they based theirs on. The code has very few comments. Repository structure is small and overseeable with their code file explanations and naming.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use two benchmark image datasets for finetuning. They also describe their sources of the pretrained models used. One data set automatically downloads, the other isnt clarified. No citations, descriptions or statistics provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the finetuning hyperparameters in appendix A. An overview on the parameters is given in the implementation's 'train.py'. The learning rate was sometimes selected from a grid. No other acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors report mean and standard deviation over accuracy in 5 random seeds. There are no specifications regarding training/testing sets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires experience in robust / adversarial learning.
