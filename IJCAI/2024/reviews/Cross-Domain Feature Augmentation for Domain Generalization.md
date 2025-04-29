
## Cross-Domain Feature Augmentation for Domain Generalization
Yingnan Liu, Yingtian Zou, Rui Qiao, Fusheng Liu, Mong Li Lee, Wynne Hsu
Keywords: Computer Vision: CV: Transfer, low-shot, semi- and un- supervised learning, Computer Vision: CV: Machine learning for vision
IJCAI/2024/Proceedings/0127 - Cross-Domain Feature Augmentation for Domain Generalization.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors share implementation details in section 4, on which library and version was used. In figure 2 they present an overview on the method. No implementation is shared. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors use 5 benchmark data sets on which they present short descriptions and cite the sources. A few statistics are given. No direct links are shared.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors share details on the training procedure per data set in section 4, and refer to previous work for some of the details. It will take some effort to verify if all needed values are presented for reproduction. The authors state a few grids on which some hyperparameters were optimised.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state they use accuracy as a metric in 4.1, and that they present the results averaged over 10 or 3 runs on the tests sets. They do not state what the variance in table 1 represents. They refer for the partitioning of the data of the experiment in part to a previous work, in part its stated in section 4. The training procedures are explained in 3.3 and 4.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires a previous experience of Computer Vision to understand the tasks/method in some parts, and to re-implement the code to conduct the experiments. Could be substantially lower by giving implementation documentation, however some details were shared on this which already helps.
