## Supervision Complexity and its Role in Knowledge Distillation
Hrayr Harutyunyan, Ankit Singh Rawat, Aditya Krishna Menon, Seungyeon Kim, Sanjiv Kumar
Keywords: 
ICLR/2023/Proceedings/10878 - Supervision Complexity and its Role in Knowledge Distillation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

No implementation provided. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(3/3)

The authors use CIFAR-10, CIFAR-100, and Tiny-ImageNet. No details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors list the learning rate per dataset/model in table 4 of appendix A. Furthermore they state various HP values there in text. Not all values are motivated.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure mean with standard deviation accuracy over three random runs on the test set. Data split not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
