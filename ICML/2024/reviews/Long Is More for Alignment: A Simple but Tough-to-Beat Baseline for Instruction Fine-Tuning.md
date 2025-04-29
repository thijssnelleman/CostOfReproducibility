
## Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning
Hao Zhao, Maksym Andriushchenko, Francesco Croce, Nicolas Flammarion
Keywords: 
ICML/2024/Proceedings/35213 - Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning.pdf
Project URL: https://github.com/tml-epfl/long-is-more-for-alignment

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link for their implementation (https://github.com/tml-epfl/long-is-more-for-alignment). In the readme they introduce the method, post news, provide instructions on how to install, details on the datasets and their files, how to run the training/evaluation code. The code could use some more comments and the repository and index on the dir/file structure.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors include datasets in their implementation. The authors use two public datasets and take a subset of them (which they explain in details with statistics and citations). Furthermore, the authors evaluate their method on Open LLM benchmark, providing six more datasets. These datasets are not directly linked. Extensive details provided in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state full hyperparameter space and values per experiment in appendix A.2. For many hyperparameter decisions the authors refer to previous works. No full budget/acquisition strategy specified however.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state evaluation details/procedure in appendix A.3. They also include human evaluation with details. The metrics are standard. The authors state the train/test splits in the appendix. Results are single model (sometimes aggregated over various datasets)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on LLM/NLP.
