
## MCSSME: Multi-Task Contrastive Learning for Semi-supervised Singing Melody Extraction from Polyphonic Music
Shuai Yu
Keywords: APP: Other Applications
AAAI/2024/Proceedings/27790 - MCSSME: Multi-Task Contrastive Learning for Semi-supervised Singing Melody Extraction from Polyphonic Music.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide any implementation source but do note that they implemented theirs using PyTorch, thus all would have to be implemented from scratch. The authors do provide clear diagrams on their method, but this would still be a costly endeavour. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors use data sets presented in other works (four for training, four for testing), which are semi-publicly openly available upon request. This raises the effort slightly. They provide statistics on the data sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

Although there are some notes in the paper regarding (hyper)parameters, there seems to be no clear specification of what the (hyper)parameters of the method are, nor what the used values are or how they were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state how the data was divided for training and testing, provide one-shot results on this procedure and give a citation on their convention. Metrics are also provided. The linked/cited evaluation library does not seem to go anywhere (the [19] in experiment set up). This is slightly confusing but should not have a substantial impact.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The data specific problems of music data would require some effort to get into. The method is defined in clear mathematical terms, but will require an experienced eye to fully grasp.