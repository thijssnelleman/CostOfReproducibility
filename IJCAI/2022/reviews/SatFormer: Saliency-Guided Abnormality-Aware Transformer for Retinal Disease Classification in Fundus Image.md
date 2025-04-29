
## SatFormer: Saliency-Guided Abnormality-Aware Transformer for Retinal Disease Classification in Fundus Image
Yankai Jiang, Ke Xu, Xinyue Wang, Yuan Li, Hongguang Cui, Yubo Tao, Hai Lin
Keywords: Computer Vision: Biomedical Image Analysis, Machine Learning: Attention Models, Machine Learning: Classification, Machine Learning: Convolutional Networks, Multidisciplinary Topics and Applications: Bioinformatics
IJCAI/2022/Proceedings/0138 - SatFormer: Saliency-Guided Abnormality-Aware Transformer for Retinal Disease Classification in Fundus Image.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors present the architecture of their method in figure 1 and an illustration on their model in figure 2. They state various details on their implementation regarding parameter values for the training process, but no practical details regarding their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/3)

The authors state they use three datasets in 4.1, one large datasets the authors collected themselves and two public datasets for which they provide citations. On the collected data set they provide statistics and subfield specific details. More details on the public data set would be welcome but can possibly be extracted through the citations. The private data set has some information, but it will be difficult to defend comparability or set up a similar acquisition based on the provided information.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state their HP values in 4.1. There is no clear summary of all HPs / search space so its not clear of all needed values are provided. There is no details on the acquisition of the values. The authors do fully state the architecture of the model (variants).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they conduct a random split of 70-10-20 tvt and use 10 fold cross validation for experiments for their private data set. They don't explicitly state the aggregation (average implied). The other data sets contain provided static splits. The authors state the used metrics as well, which are all standard.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on Transofrmers, the task (biomedical) and computer vision classification.
