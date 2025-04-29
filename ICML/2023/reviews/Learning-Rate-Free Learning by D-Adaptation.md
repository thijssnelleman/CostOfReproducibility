
## Learning-Rate-Free Learning by D-Adaptation
Aaron Defazio, Konstantin Mishchenko
Keywords: 
Award: Outstanding Paper
ICML/2023/Proceedings/341 - Learning-Rate-Free Learning by D-Adaptation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 1 (https://github.com/facebookresearch/dadaptation). The readme states details on the implementation, a changelog, experiment results, and a license file. There is an installation file given ('requirements.txt'). Comments are good, structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

The authors use CIFAR10, CIFAR100, ImageNet, IWSLT14, Book-Wiki corpus, COCO 2017, fastMRI Knee Dataset, Criteao Kaggle Display Advertising dataset. Each has a citation and a brief description but no statistics. No links in implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Hyperparameters per experiment are summarised in table format in the appendix per experiment, which are used to create models to use for their method. The input parameters for their methods are ranges of feasible values to explore so they are tuned in each experiment. Final values reported in table 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Results are presented as average and standard dev over multiple seeds. The amount of seeds is not clear. Metrics are based on the test set and are accuracy, SSIM, perplexity but not all are standard. The authors do not specify the data splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise with optimisation methods and learning rate adaptation/scheduling/optimisation.
