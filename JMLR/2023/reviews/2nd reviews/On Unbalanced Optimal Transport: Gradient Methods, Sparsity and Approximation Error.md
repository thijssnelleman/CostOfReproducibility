
## On Unbalanced Optimal Transport: Gradient Methods, Sparsity and Approximation Error
Quang Minh Nguyen, Hoang H. Nguyen, Yi Zhou, Lam M. Nguyen
Keywords: 
JMLR/2023/Proceedings/221158 - On Unbalanced Optimal Transport: Gradient Methods, Sparsity and Approximation Error.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

Implementation/Code is not given. It is not said, in which language the evaluation is coded, however it is implied that it was done using Python and they give one library that was used to calculate ground truths. There is detailed pseudocode on the method. 


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

For their simulation experiments, they do not provide code but give a detailed explanation along with the parameter choices used for data generation. 
In addition, they evaluate on the well-known CIFAR-10 and Fashion-MNIST datasets without direct links, but with citation. Also, they do not give descriptions and statistics on the datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

As far as i can understand the paper, the proposed methods do not require any hyperparameter choices, thus we do not penalise for hyperparameter choices. Epsilon and Tau seem to be parameters of the problem.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors do not introduce the used metrics really well, e.g. it is not known for inexperienced readers what the "primal gap" or "sparseness of a transportation plan" refers to. However, there is an intuition understandable to everybody. There is no train/test split since the algorithm is not trained. When the authors aggregate results, they state how the average is calculated. However, statistical information of the distribution is missing. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The paper is mostly written towards specialised readers from the field. The problem is introduced very formally and presents mostly theoretical proofs. There is no implementation available, thus the barrier of entry is even higher. While pseudo-code is provided, i believe it is only understandable for experienced readers familiar with the field. 
