## Clean-image Backdoor: Attacking Multi-label Models with Poisoned Labels Only
Kangjie Chen, Xiaoxuan Lou, Guowen Xu, Jiwei Li, Tianwei Zhang
Keywords: 
ICLR/2023/Proceedings/11656 - Clean-image Backdoor: Attacking Multi-label Models with Poisoned Labels Only.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

Authors do not provide their code. +4
Pratical details: One can find some details in the Appendix ("The victim model used in this task is taken from an open-source NLP library NeuralClassifier"). +3

Pseudocode is provided, figure shows the architecture of the method. +0


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors us VOC7, VOC12 and MS-COCO.
There are citations for each of these (=direct links). +0 
There descriptions. +0
There are statistics (e.g. no of images per categories). +0
Public datasets. +0

They use no synthetic data generators.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

Not summarised. +3
Not specified. +4
No info on aquisition. +2

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Standard metrics such as accuracy, recall, f1, details in Appendix C. +0
Evaluation on test set. +0
I miss no information concerning aggregation and strategy. +0

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Score could be higher for someone not familiar with adversarial attacks. Paper needs familiarity with multi-label classification, backdoor attacks and adversarial attacks, but not crazy theory.
