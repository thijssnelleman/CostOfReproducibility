## Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors
Ido Amos, Jonathan Berant, Ankit Gupta
Keywords: 
Award: Outstanding Paper Award
ICLR/2024/Proceedings/1909 - Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation at the end of the introduction (https://github.com/IdoAmos/not-from-scratch). The readme has installation notes, how to run experiments, where files are found and placed by the code. The structure is massive and needs a proper index. Code has good comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors use 6 tasks from LRA (cited) and describe each clearly. They install automatically in the code. Configs given in implementation per task.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide a large directory called `configs` with values per task and method. They are described in appendix C. They source most values from a previous work.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure accuracy over ratio of data provided and Maximal absolute values of kernels. Results are single runs. Not all metrics are clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
