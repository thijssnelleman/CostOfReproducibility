## D^2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning
Adyasha Maharana, Prateek Yadav, Mohit Bansal
Keywords: 
ICLR/2024/Proceedings/17608 - D^2 Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

Authors provide a link to the implementation in footnote 1 of the abstract (https://github.com/adymaharana/d2pruning). In the readme they state how to install, examples on how to run, and acknowledgements of other repositories. Code has good comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

CIFAR10, CIFAR100, Imagenet-1k, ImDB Reviews and ANLI. All are cited, and described in appendix A.1. Datasets download automatically in code and some details given in readme.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

HPs detailed in text with grid search in appendix A.3. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Authors measure accuracy, static datasplits used as specified in appendix A.1. but not stated on which is reported. Single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
