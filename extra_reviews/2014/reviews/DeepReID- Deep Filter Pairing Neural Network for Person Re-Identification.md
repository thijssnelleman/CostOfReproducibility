## DeepReID- Deep Filter Pairing Neural Network for Person Re-Identification
Wei Li, Rui Zhao, Tong Xiao, Xiaogang Wang
Keywords:
extra_reviews/2014/Proceedings/DeepReID- Deep Filter Pairing Neural Network for Person Re-Identification.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors state in section 6 that "the implementation is publicly available" but it is unclear whether they refer to their implementation of their method. After investigating, a repository linked to this work can be found but was created (2020-12-16) after the reproduction experiment (2018) and also seems to be developed not by the authors of this work. The authors provide extensive diagrams and examples on their work (fig. 1-5). No practical details except that they used a "GTX670 GPU".

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use their CUHK03 (link provided), and also use VIPeR, i-LIDS, CAVIAR, Re-ID 2011, GRID, CUHK01, CUHK02 and provide comparative statistics in table 1. They also use CUHK01 for evaluation. They describe their dataset in sec 5. All the other datasets are cited. Statistics are relatively limited.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[8]

The authors detail the model architecture in section 3. The parameter settings are presented in table 2, which contains values for data augmentation. The author state the architecture was designed using the validation set, but budget is not given. For the other parameters this is not specified, such as learning rate.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors state the proportional dataset split in section 6 for their dataset, which is randomly repeated for 20 runs. Another experiment was conducted where the training set absorbed the validation set. The splits of the CUHK01 datasets are specified in 6.3. Authors measure identification rate, and relative rank over accuracy. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
