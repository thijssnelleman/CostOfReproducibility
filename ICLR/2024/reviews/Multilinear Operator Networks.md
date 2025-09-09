## Multilinear Operator Networks
Yixin Cheng, Grigorios Chrysos, Markos Georgopoulos, Volkan Cevher
Keywords: 
ICLR/2024/Proceedings/18326 - Multilinear Operator Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

Authors provide implementation link in the abstract (https://github.com/Allencheng97/Multilinear_Operator_Networks). Readme has install notes, where to download data and place it in the file structure, how to run code and download link for model checkpoint, code acknowledgements. Code has okay comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

CIFAR10, SVHN, Tiny ImageNet1K, Oxford Flower102. Citations for all. Detailed descriptions and statistics in appendix L.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values for imagenet detailed in appendix K, table 15. It stated its for imagenet so the values for the other datasets could be different. No acquisition.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Accuracy on validation set, single model. Data splits in appendix L.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
