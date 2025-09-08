## One Transformer Can Understand Both 2D & 3D Molecular Data
Shengjie Luo, Tianlang Chen, Yixian Xu, Shuxin Zheng, Tie-Yan Liu, Liwei Wang, Di He
Keywords: 
ICLR/2023/Proceedings/12159 - One Transformer Can Understand Both 2D & 3D Molecular Data.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors state their implementation link in the abstract (https://github.com/lsj2408/Transformer-M). The readme contains an overview of the method an an updates log, how to install the code, where to download model checkpoints, where to download preprocessed data, how to run the code. The structure is large and difficult to oversee. Comments look ok.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

PCQM4Mv2 from OGB Large-Scale Challenge, PDBBind and QM9, all have citations and brief descriptions. Download link in implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values described in text in appendix B per dataset. Acquisition not given per parameter. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Authors measure MAE, RMSE, Pearsons R and std dev. Data splits specified in appendix B. Variation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
