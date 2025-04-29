
## Learning a Spiking Neural Network for Efficient Image Deraining
Tianyu Song, Guiyue Jin, Pengpeng Li, Kui Jiang, Xiang Chen, Jiyu Jin
Keywords: Computer Vision: CV: Image and video synthesis and generation, Computer Vision: CV: Applications, Computer Vision: CV: Computational photography
IJCAI/2024/Proceedings/0139 - Learning a Spiking Neural Network for Efficient Image Deraining.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/MingTian99/ESDNet). Here they describe in the readme their method with a visualisation, two tables regarding data downloading and pretrained models both with direct links, installation instructions including how to place the data into their structure, and how to train, test and evaluate the code. The code has some comments but could definetily use more. They provide a section dedicated to the implementation details in their paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors use five public data sets and provide citations on them. A short description with some statistics are given per data set with a quantity description. Each data set has a download link provided in the implementation docs. Could use more details on the data, but in general this is very accesible.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state their hyperparameter values in the paper per data set, and default values are present in the implementation but not per experiment. No details are given on how these values are acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use two 'common evaluation metrics' for which they provide citations, and a description on how its computed with a citation. They use two more metrics for the real world data sets which they cite and describe shortly. The authors describe the training and testing splits in the datasets section, which are static (Provided by the source). The results indicate single model/run results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires a good understanding of the task to understand the experiments presented, as well as the complicated and layered method.
