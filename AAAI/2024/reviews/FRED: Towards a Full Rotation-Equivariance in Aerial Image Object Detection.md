
## FRED: Towards a Full Rotation-Equivariance in Aerial Image Object Detection
Chanho Lee, Jinsu Son, Hyounguk Shon, Yunho Jeon, Junmo Kim
Keywords: CV: Object Detection & Categorization
AAAI/2024/Proceedings/28144 - FRED: Towards a Full Rotation-Equivariance in Aerial Image Object Detection.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors do not provide source code of their implementation. They do cite other papers that they used as a basis for their framework. The authors provide diagrams, and state that pseudo code should be available in the appendix (None present in AAAI version, maybe on Arxiv but that is not linked). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a benchmark data set, cite the source and provide a description on the data. They specify they use two versions of the data set and highlight the differences. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors specify details on the architecture, the employed loss function, and edge constraint loss value. However, a full description on the hyperparameters of the method is missing and could thus take a lot of effort to determine. Furthermore, no acquisition method is specified for the presented hyperparameter values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors do not specify the experimental procedure, but present single values per class in their results table, seemingly indicating a one-shot evaluation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Although the method is well formulated, it does require independent investigators a level of expertise regarding computer vision. The lack of documentation regarding the implementation severely increases this as the independent investigator would have to research how this can be implemented.
