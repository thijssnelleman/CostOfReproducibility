
## Jump Gaussian Process Model for Estimating Piecewise Continuous Regression Functions
Chiwoo Park
Keywords: 
JMLR/2022/Proceedings/211472 - Jump Gaussian Process Model for Estimating Piecewise Continuous Regression Functions.pdf
Project URL: https://www.chiwoopark.net/code-and-dataset

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a project page on JMLr where they link their code (https://drive.google.com/file/d/1XLQTd0XdqQPQ3f5jLM1aJsb3eL2lO5Eh/view). The code has a few details in the readme but no index or installation instructions. Comments are good.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(9/9)

The authors evaluate on toy five toy examples in section 3 which they provide the simulation for in their code but details are a bit lacking. In section 4 with higher dimension and its well explained and code is available. Section 5 has three benchmark datasets and describe them but details are a bit lacking, data is available in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

There are some parameters specified in algorithm 1/2 (such as tolerance) but its values are not specified. They could maybe be extracted from the code. It will take quite some effort.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure accuracy/MSE over 10/100 replications as box plots and evaluate them over test sites. In section 5 they evaluate MSE and provide the dataset splits and state they evaluate on the test set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on piecewise/jump regression.
