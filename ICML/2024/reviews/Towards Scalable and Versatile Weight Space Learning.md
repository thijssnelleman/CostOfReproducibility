
## Towards Scalable and Versatile Weight Space Learning
Konstantin Schürholt, Michael Mahoney, Damian Borth
Keywords: 
ICML/2024/Proceedings/32815 - Towards Scalable and Versatile Weight Space Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their implementation (https://github.com/HSG-AIML/SANE). In the readme they summarise the method, describe the structure of the directory/files, how to download the data and use it in the implementation, and various examples on how to run the code. The code is well documented with comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

The authors use 7 public datasets to create 'zoos' for their method. There are summaries on the zoos but not on the individual datasets. There are no  statistics or citations but download scripts for half of them.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Hyperparameter values regarding architecture are available in table 8 of appendix B. The authors state they use ray.tune (lib with citation) for optimisation, the code is available in the implementation. No budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method using accuracy epoch and ggap. The latter is not very standard. The data split is defined in section 3. The data is aggregated over the population results in table 3 and 4, presenting the mean and the standard deviation. The details of this population are a bit obscure which is possibly due to the complexity of the paper.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise in weight space learning. 
