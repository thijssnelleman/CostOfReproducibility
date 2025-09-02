## BadPre: Task-agnostic Backdoor Attacks to Pre-trained NLP Foundation Models
Kangjie Chen, Yuxian Meng, Xiaofei Sun, Shangwei Guo, Tianwei Zhang, Jiwei Li, Chun Fan
Keywords: 
ICLR/2022/Proceedings/6220 - BadPre: Task-agnostic Backdoor Attacks to Pre-trained NLP Foundation Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

No implementation (details) given. High level overview in figure 1. Pseudo code in appendix A.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use GLUE, SQuAD V2.0 and CoNLL-2003 (citations provided) and describe for which tasks they are selected. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors conduct an analysis on a grid of HP values in table 5 of appendix C. Some more HP values can be found in 5.1. A structured overview is missing and it is unclear if all needed values are reported.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Metrics are explained in 5.1. Results are single run. Results are on test set but its unclear where this test set comes from.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
