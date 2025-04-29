
## Contextual Bandits with Large Action Spaces: Made Practical
Yinglun Zhu, Dylan Foster, John Langford, Paul Mineiro
Keywords: 
ICML/2022/Proceedings/16993 - Contextual Bandits with Large Action Spaces: Made Practical.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/pmineiro/linrepcb). The main readme is empty. The other readme indexes the files and explains hyperparameter search and also provided a download link to the data. There are some notes in the notebooks regarding the code but not a lot.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide direct links in the implementation to download the data. They briefly summarise the dataset statitstics in table 1. They discuss and cite the data sets in section 5, and describe them more extensively in appendix E.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state in the implementation they optimised in amazon-3m using random search. They also reiterate that they did this for each algorithm in the appendix D. They state they evaluate 59 randomly selected configurations with a fixed seed. The authors state the parameters in the pseudo code 1,2,3 and 4. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate each algorithm on 32 sees and report CIs with 90% bootstrap for the mean. The metric is average progressive reward. Data split not applicable (no training). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on bandits.
