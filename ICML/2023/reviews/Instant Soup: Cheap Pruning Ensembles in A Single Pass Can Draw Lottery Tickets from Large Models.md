
## Instant Soup: Cheap Pruning Ensembles in A Single Pass Can Draw Lottery Tickets from Large Models
Ajay Jaiswal, Shiwei Liu, Tianlong Chen,  Ding, Zhangyang “Atlas” Wang
Keywords: 
ICML/2023/Proceedings/1501 - Instant Soup: Cheap Pruning Ensembles in A Single Pass Can Draw Lottery Tickets from Large Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors share a link to their implementation (https://github.com/VITA-Group/instant_soup). In the readme they state figures from the method. There are two other empty readme files. An environment file can be found. The code has few comments and the structure is hard to oversee. No examples etc given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(15/15)

The authors use 6 vision and 9 language benchmark datasets. Most of the datasets seem to automatically download in the implementation (direct link). Citations are provided. Explanations/statistics missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters per pretrained model (experiment) used. The possible parameters are easily found in the implementation. Acquisition of these values are not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors present the results averaged over three runs with standard deviation. Evaluation metrics are standard and cited but not clearly stated what these are. It is suggested that test sets are used but not specified how they are acquired. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with large model fune tuning. 
