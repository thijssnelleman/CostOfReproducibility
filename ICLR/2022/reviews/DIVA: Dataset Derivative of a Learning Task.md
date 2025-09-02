## DIVA: Dataset Derivative of a Learning Task
Yonatan Dukler, Alessandro Achille, Giovanni Paolini, Avinash Ravichandran, Marzia Polito, Stefano Soatto
Keywords: 
ICLR/2022/Proceedings/7196 - DIVA: Dataset Derivative of a Learning Task.pdf
Project URL: https://openreview.net/attachment?id=bVvMOtLMiw&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors provide supplementary material which contains only the appendix. High level overview given in figure 1. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

The authors use pretrained models on ImageNet, Places365 and use in their experiment CUB-200, FGVC-Aircraft, Stanford Cars, Caltech-256, Oxford Flowers 102, MIT-67 Indoor, Street View House Number and Oxford Pets. All have citations provided. More dataset details given in appendix B. No direct links or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The method of the paper seems to only (re)use the learning rate parameter alpha. Their method optimises HP values as well. Some more values are stated in the appendix B. A structured overview is missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors state they used default dataset splits and for those who did not provide (Oxford Flower and Caltech-256) how they created these. The authors present test error in table 1, f1 score and AUC in figure 3. Results seem to be single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[8]

-
