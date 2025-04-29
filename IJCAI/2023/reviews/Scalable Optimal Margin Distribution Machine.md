
## Scalable Optimal Margin Distribution Machine
Yilin Wang, Nan Cao, Teng Zhang, Xuanhua Shi, Hai Jin
Keywords: Machine Learning: ML: Classification, Data Mining: DM: Big data and scalability, Machine Learning: ML: Kernel methods
IJCAI/2023/Proceedings/0485 - Scalable Optimal Margin Distribution Machine.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors share a link to their implementation (https://github.com/CGCL-codes/SODM). In the readme, the authors introduce the method and how to build and run an example. The repository is quite large and could use an index to guide the reader through it. The code has some comments. It will take some effort to understand the flow of the code, partially due to the size of the project and partially due to the minor documentation in the readme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[9]

(0/8)

In section 4.1 the authors introduce 8 datasets, state that they are real-world, and summarise some base statistics in table 1. No citations or links are provided, neither in the paper nor in the implementation. It is not possible to verify these datasets are public based on the paper, thus we assume they are privte. The details shared are quite minor.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The auhotrs state three parameters in algorithm 1, and four in algorithm 2 some of which overlap. No values are stated that were used for the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the data division is done 80-20 at random for each experiment. The results indicate single runs. The used metrics (Accuracy and training time) are straight forward. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires an understanding on scalable machine learning.
