
## Distinguishing the Knowable from the Unknowable with Language Models
Gustaf Ahdritz, Tian Qin, Nikhil Vyas, Boaz Barak, Benjamin Edelman
Keywords: 
ICML/2024/Proceedings/32819 - Distinguishing the Knowable from the Unknowable with Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/KempnerInstitute/llm_uncertainty). In the readme they introduce the method, provide instructions how to acquire the pretrained models, a brief index on the code files, how to run the code with various parameters. The code has a decent amount of comments. There is an installation/requirements file available. An overview of the method is presented in figure 1 and 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

There is a data file available in the implementation. The authors take a large dataset, split it into three subsets, provide samples on each dataset in appendix J. Citations and description are provided in 3.3. Statistics are missing. Direct links are not given for the large set nor the three subsets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors sate 'with minal hp tuning it is possible to train accurate classifiers'. Furthermore the authors state later in 5.1 they choose hyperparameters such that copying of examples in the model's promt is allowed. In the appendix there is a small mention regarding hyperparameter settings. From the implementation all hyperparameters are easily extractable with default values but these would have to be assumed to be overlapping. No acquisition really clarified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use AUC and accuracy as metrics. The results are single model. The authors use the test set provided by the datasets (static).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on LLM and NLP.
