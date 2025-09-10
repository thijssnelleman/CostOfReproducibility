## On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes
Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos Garea, Matthieu Geist, Olivier Bachem
Keywords: 
ICLR/2024/Proceedings/19484 - On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

Implementation not provided. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

XSum, WMT14, GSM8K, citations and breif descriptions for all.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors provide HP values per experiment in section 4 and appendix A, tables A.1-A.4. For WMT they refer to a previous work for the selected values, but not for all it is specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Average across three seeds for some others not clear, reporting ROUGE-2, test accuracy, values reported on validation/test splits of datasets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
