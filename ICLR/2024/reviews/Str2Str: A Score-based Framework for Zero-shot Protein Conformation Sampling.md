## Str2Str: A Score-based Framework for Zero-shot Protein Conformation Sampling
Jiarui Lu, Bozitao Zhong, Zuobai Zhang, Jian Tang
Keywords: 
ICLR/2024/Proceedings/19188 - Str2Str: A Score-based Framework for Zero-shot Protein Conformation Sampling.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to the implementation in the abstract (https://github.com/lujiarui/Str2Str). Readme has installation instructions, how to download data and what file structure to use, examples on running the code, checkpoint download link, contact details. Code has good comments. Structure is large and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

FAST FOLDING PROTEINS, BPTI, both cited, download scripts in implementation, described but no statistics. PDB used for training, see appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Hyperparameter values listed in table S7. There are many configuration files present in the implementation. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Evaluation metrics detailed in 4.1. and appendix E. Results are averaged across all targets. Training split based on datasets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
