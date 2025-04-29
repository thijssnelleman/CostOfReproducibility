
## Align, Perturb and Decouple: Toward Better Leverage of Difference Information for RSI Change Detection
Supeng Wang, Yuxi Li, Ming Xie, Mingmin Chi, Yabiao Wang, Chengjie Wang, Wenbing Zhu
Keywords: Computer Vision: CV: Scene analysis and understanding
IJCAI/2023/Proceedings/0166 - Align, Perturb and Decouple: Toward Better Leverage of Difference Information for RSI Change Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/wangsp1999/CD-Research/tree/main/openAPD). In the readme they have very brief statements on how to install, fetch the data, how to train/test and get the results. The configurations have their own code files. The code has some comments. In general the implementation could do with some more documentation as the file structure is quite large, thus increasing the effort of understanding the flow of the code. More implementation details are stated in 4.1. The authors provide a framework design in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors include direct download instructions in the implementation docs. The authors state the data sets used in 4.1, with citations, descriptions and some minor statistics. More details would be welcome. In general its made very easily available by the authors thus lowering the cost for comparability.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in 4.1. A full summary of the configuration can be found in the implementation docs. However no explanation is given on how these values were acquired. In section 4 they do a verification of parameter sensitivity on one of the parameters (ablation study).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The evaluation metrics are stated in 4.1, which are quite standard. The authors state the t.v.t splits in 4.1 and indicate they are static/provided. The results are single runs/models.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries an understanding on CV and the task.
