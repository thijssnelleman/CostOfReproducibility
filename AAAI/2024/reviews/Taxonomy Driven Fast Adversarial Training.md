
## Taxonomy Driven Fast Adversarial Training
Kun Tong, Chengze Jiang, Jie Gui, Yuan Cao
Keywords: CV: Adversarial Attacks & Robustness, ML: Adversarial Learning & Robustness, CV: Scene Analysis & Understanding
AAAI/2024/Proceedings/28648 - Taxonomy Driven Fast Adversarial Training.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/bookman233/TDAT). Here the authors provide their source code with requirements/dependencies, an small example on how to run the code, training logs of their own runs, and a small index for their directories. The code itself however seems without comments making it more difficult to understand the flow of the process and design choices. The authors provide a taxonomy in their paper and pseudo code which negates this in part. Furthermore in their methodology section they provide a substantial explanation on their implementation of the method. If the documentation in the code/repository were improved, this should be a 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use 4 datasets which 'are standard for AT'. They cite their sources, but provide no details or statistics on the data sets nor do they provide links to the data sets (including the implementation documentation). However, since these are quite widely known data sets, this should not be a real big effort to find. Also the authors provide their data loaders.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide extensive details on their training details, including in the implementation documentation. They document the hyperparameters of each data set in the paper, and refer for more details to the supplementary materials. There are default values present for HP's as well in the implementation documentation. How these values were acquired is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors provide some details in their experimental set up regarding training, but specifications are a bit difficult to extract. However, with the presented implementation documentation this is possible.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The authors dive straight into the domain of adversarial learning, and present their rather complex algorithm with many details. There are not many examples. This is not a criticism of the paper however, rather a combination of method complexity and presentation design choice of the authors.
