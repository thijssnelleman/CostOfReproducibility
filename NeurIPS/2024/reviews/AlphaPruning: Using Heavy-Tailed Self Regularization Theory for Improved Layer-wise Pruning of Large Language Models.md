
## AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models
Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang &quot;Atlas&quot; Wang, Michael Mahoney, Yaoqing Yang
Keywords: 
NeurIPS/2024/Proceedings/94217 - AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a pipeline diagram in figure 1. The authors provide a link to their implementation (https://github.com/haiquanlu/AlphaPruning). In the readme they introduce the method, post updates, provide installation notes (separate markdown file), download links for pre-computed metrics, how to run a script to reproduce a table from their paper, explanation of arguments of their code, a download link for a framework used in their source code and explanation on how it impacts specific parts of the code, more examples for fine-tuning with args explanations, an explanation on one of the directories. The code has decent comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors evaluate pretrained LLMs on WikiText validation set. A citation is given for this dataset, but no descriptions or statistics. The dataset downloads automatically in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide the hyperparameter settings in appendix G and give the values per experiment in table 8. They state in the caption they conducted gridsearch with grids provided. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors discuss the metrics and their definitions in 2.2. The authors define them over 'perplexity' (subfield specific) and average accuracy over 7 zero shot tasks. The results are single models. Train/test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on LLMs and pruning with the latest techniques.
