
## Oracle-Efficient Reinforcement Learning for Max Value Ensembles
Marcel Hussing, Michael Kearns, Aaron Roth, Sikata Sengupta, Jessica Sorrell
Keywords: 
NeurIPS/2024/Proceedings/95670 - Oracle-Efficient Reinforcement Learning for Max Value Ensembles.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provided their implementation through supplementary material (https://proceedings.neurips.cc/paper_files/paper/2024/file/d560f94c582033e6d8eb0c97cdd4f721-Supplemental-Conference.zip). In the readme they state installation notes, a direct link to the data and how to run the code as well as how to change the configuration. The code does not have a lot of comments but the most critical parts seem to be documented well. Pseudo code is given in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors provide a link to the datasets used in the implementation and appendix (https://datadryad.org/dataset/doi:10.5061/dryad.9cnp5hqps). The authors state the environment used and offline datasets with citations in section 5. The environment is described with great detail. The datasets are offline versions of the environment. Statistics on it are not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors summarise the hyperparameter values in appendix C.1. table 1 & 2 including architectures. The values are also summarised in the implementation. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method with mean performance and standard error over 5 seeds with 32 episode evaluation. Metrics are environment return and successrate. Train/test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise in RL.
