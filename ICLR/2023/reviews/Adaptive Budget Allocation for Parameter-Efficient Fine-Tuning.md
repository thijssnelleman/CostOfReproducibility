## Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning
Qingru Zhang, Minshuo Chen, Alexander Bukharin, Pengcheng He, Yu Cheng, Weizhu Chen, Tuo Zhao
Keywords: 
ICLR/2023/Proceedings/11863 - Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning.pdf
Project URL: https://openreview.net/attachment?id=lq62uWRJjiY&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/QingruZhang/AdaLoRA). Pseudo code in appendix A algorithm 1. The readme has an overview of the directories, a quickstart with installation instructions and examples on how to use the code including explanation of parameters, how to run the code on a benchmark datasets. The code is in general well documented with readmes and comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use GLUE, SQuADv1 and SQuADv2, XSum, CNN/DailyMail. All have citations provided. Extensive GLUE dataset details in appendix D but not for all. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide tables of hyperparameter settings in appendix E, F and G per dataset. The authors specify grids overwhich they were tuned.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report the mean over 5 runs on the development set and measure EM/F1/Acc/Mcc/Corr/Ave.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
