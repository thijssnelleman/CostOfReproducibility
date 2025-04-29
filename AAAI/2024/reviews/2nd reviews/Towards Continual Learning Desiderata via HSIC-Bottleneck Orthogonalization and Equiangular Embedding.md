## Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding
Depeng Li, Tianqi Wang, Junwei Chen, Qining Ren, Kenji Kawaguchi, Zhigang Zeng
Keywords: ML: Life-Long and Continual Learning, ML: Time-Series/Data Streams, ML: Classification and Regression, ML: Other Foundations of Machine Learning
AAAI/2024/Proceedings/30358 - Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

- The authors do not provide a link for the source code implementation; this increases the cost by 4.
- The authors state that all experiments are run in PyTorch, without any other details on the framework; this increases the cost by 3.
- The authors provide a detailed pseudocode of their algorithm and a general blueprint of the architecture (which is not extremely detailed). This increases the cost by 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

- The authors use the following datasets: 3 small-scale (MNIST, FashionMNIST and CIFAR-10); 1 medium-scale (CIFAR-100) and 1 large-scale (ImageNet-R). There is no direct link present to where the data can be downloaded (cost increased by 1).
- The citation and descriptions are provided, and since all dataset (maybe only except the large-scale one, which actually contains more information) are very well-known image classification datasets, even without statistics detailed I argue that they are introduced in enough detail (but still increasing the cost by 1). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

- The authors take the suggested hyperparameter values for different modules of their methods based on various prior works, but do not perform additional hyperparameter tuning. The hyperparameter spaces are therefore not provided; cost increased by 3. 
- While in general not a good practice, they do state a single value for each required HP, which in my opinion makes it sufficient to at least know how to set those HPs to hopefully arrive to the same conclusions.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

- The authors measure accuracy, which is very standard, although I failed to find this explicitly stated in the experimental setup section; it is rather stated in the figure captions and somewhat implied.
- There is a specification on the train/test and it is clear how the dataset is split (default proposed splits for each dataset). But there is still some mystery regarding validation set, as it seems it was never used -- as there are not enough details on validation, cost increased by 1.
- No details on the strategy for evaluations, in my opinion it is kind of implied, but I am really not sure how they do it. Probably some form of cross-validation... cost increased by 2.
- It is clear how the results are aggregated (again only through figure captions), but variance is not explained. Cost increased by 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

I found this paper quite all over the place and it does require deep expertise in several sub-domains to be able to reproduce the results and arrive to the same conclusions. In terms of experiments, they also need to be implemented from scratch, and there is some missing info on different experimental aspects. In total, I give it a cost of 7.