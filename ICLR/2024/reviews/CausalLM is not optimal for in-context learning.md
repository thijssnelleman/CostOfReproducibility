## CausalLM is not optimal for in-context learning
Nan Ding, Tomer Levinboim, Jialin Wu, Sebastian Goodman, Radu Soricut
Keywords: 
ICLR/2024/Proceedings/18127 - CausalLM is not optimal for in-context learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

Code not provided. They provide a link in the appendix on which htey based their code as a starting point.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[9]

(0/1)

The authors use an ICL dataset of 64k sequences and provide little other detail.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

In appendix E, the authors refer mainly to a previous work for their HP settings. A summary in text is given, although it is difficult to determine if all needed values are there. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

They measure MSE error over number of layers, results are single run. The authors report on a 64 out of 64k holdout test set of the dataset. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
