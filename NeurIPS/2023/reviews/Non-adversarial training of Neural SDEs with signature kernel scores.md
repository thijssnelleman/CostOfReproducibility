
## Non-adversarial training of Neural SDEs with signature kernel scores
Zacharia Issa, Blanka Horvath, Maud Lemercier, Cristopher Salvi
Keywords: 
NeurIPS/2023/Proceedings/70714 - Non-adversarial training of Neural SDEs with signature kernel scores.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors link a github package they used for their rough bergomi data processing in the appendix. They submit the code as supplementary material (https://openreview.net/attachment?id=ixcsBZw5pl&name=supplementary_material). In the readme they link the nobtebooks they used for their experiments in the paper. There is an installation file included. The code has okay comments. The structure is overseeable with their notes in the readme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(4/5)

The authors state the datasets in sec 4, that they use 5 datasets. Three are synthetic. The forex data set is included in the implementation (and linked in the paper), one generator is linked in the appendix. There are generators available in the code as well but it will take some effort to determine which is which. The NASDAQ data set cannot be found. The descriptions on the datasets are too brief. They do state the variables of each generation before the experiment. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the HP values in the appendix per data experiment. Structured overview missing. No acquisition strategy given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors repeat each test 5000 times and report the average. The metrics are KS score and Type I error, they provide a citation for these but no explanation. There are mentions of train and test set in the paper, but its not clarified completely per task.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on stochastic differential equation models, and kernels.
