## iSuc-PseOpt- Identifying lysine succinylation sites in proteins by incorporating sequence-coupling effects into pseudo components and optimizing imbalanced training dataset
Jianhua Jia, Zi Liu, Xuan Xiao, Bingxiang Liu, Kuo-Chen Chou
Keywords: Lysine succinylation, Sequence-coupling model, PseAAC, Optimize training dataset, Target cross-validation
extra_reviews/2016/Proceedings/iSuc-PseOpt- Identifying lysine succinylation sites in proteins by incorporating sequence-coupling effects into pseudo components and optimizing imbalanced training dataset.pdf
http://www.jci-bioinfo.cn/iSuc-PseOpt

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors do not provide their implementation: the project page yields an error (http://www.jci-bioinfo.cn/iSuc-PseOpt). However, the authors do not introduce a new method/algorithm here, but rather create a pipeline using three existing methods to evaluate their effectiveness. They state they develop in Matlab and link the code for the Random Forest implementation used in their method, which is the most crucial element. However, this still means substantial work will have to be done by the independent investigators. They state how they use KNN to clean the dataset first, and IHTS to generate new samples for the dataset (data preprocessing). This is quite clearly stated, and are relatively standard/common techniques.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use CPLM, a protein lysine modiﬁcation database and provide a citation. The data is described at length, and provide supplementary materials containing the positive subset of this dataset. They do not provide a link to the rest of the dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors state the parameter values used, and refer to the original works for some details. As their own method is the pipeline, the values matter somewhat less and can be deduced from the original work. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors define their metrics with formulae in eq. 14. The authors detail the data split strategy and how cross validation was applied, and results were averaged.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[1]

-
