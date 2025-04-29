
## Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards
Alexandre Rame, Guillaume Couairon, Corentin Dancette, Jean-Baptiste Gaya, Mustafa Shukor, Laure Soulier, Matthieu Cord
Keywords: 
NeurIPS/2023/Proceedings/70592 - Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/alexrame/rewardedsoups). In the readme they introduce the method and describe the experiments. There is a requirements file for installation. The code needs more comments and the structure is large without an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

The authors use Reuters news and Reddit TL;DR in figure 1b and 2a (citations given) and also Stack Exchange questions in fig 2c (citation given), movie review generation (no citation) and helpfulness as a conversational assistent (citation given) as well as COCO and Karpathy split. No description or statistics or direct links given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are summarised per dataset in table 1 and also link the figures they relate to. No acquisition given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors evaluate with various metrics, most are standard but some require more explanation. The results are single model. Data splits not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on NLP tasks and RL crossover.
