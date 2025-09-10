## Set Learning for Accurate and Calibrated Models
Lukas Muttenthaler, Robert A Vandermeulen, Qiuyi (Richard) Zhang, Thomas Unterthiner, Klaus R Muller
Keywords: 
ICLR/2024/Proceedings/18987 - Set Learning for Accurate and Calibrated Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to the implementation in footnote 1 of the introduction (https://github.com/LukasMut/OKO). Readme has an example of running the code but nothing else. There is a requirements file detailing installation requirements. Code can use more comments and a structure index for the files.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

MNIST, FashionMNIST, CIFAR-10, CIFAR-100. No citations or any other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values selected on a heldout validation set, but values not specified in the paper. There are values available in the code but it will take some effort to find each per experiment. Budget not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors measure test accuracy on the official test sets of the dataset. Results over 5 random seeds averaged with 95% CI.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
