
## Revealing Hierarchical Structure of Leaf Venations in Plant Science via Label-Efficient Segmentation: Dataset and Method
Weizhen Liu, Ao Li, Ze Wu, Yue Li, Baobin Ge, Guangyu Lan, Shilin Chen, Minghe Li, Yunfei Liu, Xiaohui Yuan, Nanqing Dong
Keywords: Multidisciplinary Topics and Applications: General, Computer Vision: General, Machine Learning: General
IJCAI/2024/Proceedings/0815 - Revealing Hierarchical Structure of Leaf Venations in Plant Science via Label-Efficient Segmentation: Dataset and Method.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present a link to their implementation (https://github.com/WeizhenLiuBioinform/HALVS-Hierarchical-Vein-Segment). In the readme the authors present their method, an overview of the repository, motivation/design, a direct link to the data set + explanation on the data and environment details / installation instructions. The models have seperate readmes in their respective directories. The code could do with more comments in some files. The authors provide details on the implementation in the paper as well in section 5.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors collect their own data set and publish download links in the implementation docs with instructions. Full descriptions and details are given in section 3. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors evaluate three baselines from other works on their data set. Full config files are given in the implementation docs. They cite two sources for their hyperparameter choices, but not all are explained how they were achieved. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the training procedure and the metrics used for evaluation. However details on how the data was divided into training/testing is not given in the paper, suggesting it is training results presented. The implementation docs seem to confirm this, but it will take some effort to verify.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires an understanding of the subject matter (biology/leaf veins) to understand the task + CV/image segmentation.
