## Information-theoretic Online Memory Selection for Continual Learning
Shengyang Sun, Daniele Calandriello, Huiyi Hu, Ang Li, Michalis Titsias
Keywords: 
ICLR/2022/Proceedings/5961 - Information-theoretic Online Memory Selection for Continual Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors state in their reproducibility statement that they provide detailed pseudo code in algorithm 1 and 2. However, not much else regarding implementation is given.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors use (permuted/split) MNIST, CIFAR10 and MiniImageNet, for which they provide details in section 5. Citations/links/statistics are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors state the HP values in text in section 5, as well as a tabular overview in table 1 of the appendix. The authors also state they selected the best HP values using averaged validation accuracy across 5 random seeds, the grids are given in table 1.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report the average over 10 seeds on the test set. They report accuracy. They plot the mean + 95% CI. It is clear how the validation set is created, but not exactly where the train/test split comes from.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
