## Scale Mixtures of Neural Network Gaussian Processes
Hyungi Lee, Eunggu Yun, Hongseok Yang, Juho Lee
Keywords: 
ICLR/2022/Proceedings/6289 - Scale Mixtures of Neural Network Gaussian Processes.pdf
Project URL: https://openreview.net/attachment?id=YVPBh4k78iZ&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their implementation in appendix H, footnote 3 (https://github.com/Anonymous0109/Scale-Mixtures-of-NNGP), which gives a 404 error which seems a mistake of the authors as it is still the anonymous link from the review. A quick search resolves this to a correct github repository (https://github.com/yuneg11/Scale-Mixtures-of-NNGP). There is little usefull information in the readme, and no installation information. The code has no comments and there is no explanation on the structure or how to run the code.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors use the UCI dataset and provide a link, as well a SVHN, MNIST, KMNIST, FMNIST and CIFAR10 for which no links or citations are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors state architecture details in 4.1 in text. There are some hyperparameter details in appendix G and the authors state they chose the best values based on the validation set but exactly how this is done is not clear. No structured overview available.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

The authors state in appendix G how train/validation/test split is done. The authors measure NLL, accuracy on the datasets, aggregation/variation/population not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
