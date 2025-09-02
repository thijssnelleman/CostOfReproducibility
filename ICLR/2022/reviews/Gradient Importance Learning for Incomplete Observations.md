## Gradient Importance Learning for Incomplete Observations
Qitong Gao, Dong Wang, Joshua Amason, Siyang Yuan, Chenyang Tao, Ricardo Henao, Majda Hadziahmetovic, Lawrence Carin, Miroslav Pajic
Keywords: 
ICLR/2022/Proceedings/6859 - Gradient Importance Learning for Incomplete Observations.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in a footnote on the first page (https://github.com/gaoqitong/gradient-importance-learning). The readme contains contact details, installation notes, and a statement of providing code on how to run it but this is not present here but in seperate readmes in the other directories including explanations on all the options of the entry points. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use MIMIC-III, a de-identified ophthalmic patient dataset obtained from an eye center in North America and MNIST. Citations provided for the first and the last. A foruth dataset is only used for the appendix and thus not included in the cost here. Descriptions are brief, but much more extensive in the appendix D, where a link is provided for MIMIC-III. The patient dataset is available in the implementation, but only the test set (training can be requested).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors document the HP and values in the appendix per dataset in the text. They specify grid searches for certain HPs. For other methods they use the values presented by the authors. Structured overview not given.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure accuracy and AUC over 3 random masks with average and std dev. Data splits specified in section 4 and appendix D.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
