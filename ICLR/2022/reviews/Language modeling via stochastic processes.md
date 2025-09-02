## Language modeling via stochastic processes
Rose Wang, Esin Durmus, Noah Goodman, Tatsunori Hashimoto
Keywords: 
ICLR/2022/Proceedings/5950 - Language modeling via stochastic processes.pdf
Project URL: https://openreview.net/attachment?id=pMQwKL1yctf&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in a footnote of the abstract (https://github.com/rosewang2008/language_modeling_via_stochastic_processes). The readme is structured well, and contains information on the method, how to install, how to use the datasets, examples on how to run experiments, where to find output files, and how to re-run their analysis. The repository structure is large, but the decoder directory for example is a link to another repo with its own indexing. Yet the amount of comments also seems to be a bit lacking here and there. So it will still take some effort to navigate and understand.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The implementation contains four (TM2, TicketTalk, ) datasets, and provides download instructions for the other two (Wikihow, Recipe NLG). Extensive dataset information is given in appendix E.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

A few hyperparameter and architecture values are stated in section 4 in the text. Acquisition is not specified but structured configuration files per experiment are available in the implementation.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report mean + std dev of accuracy over three runs. They also report BLEU (standard) mismatch (MM, explained in appendix E). The train-test splits are static (appendix E) and provided in the code. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
