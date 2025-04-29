
## GOCPT: Generalized Online Canonical Polyadic Tensor Factorization and Completion
Chaoqi Yang, Cheng Qian, Jimeng Sun
Keywords: Data Mining: Mining Spatial and/or Temporal Data, Constraint Satisfaction and Optimization: Solvers and Tools, Data Mining: Mining Data Streams, Machine Learning: Online Learning
IJCAI/2022/Proceedings/0326 - GOCPT: Generalized Online Canonical Polyadic Tensor Factorization and Completion.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors open source their code online (https://github.com/ycq091044/GOCPT) and publish it as a PyPi package as well. The readme has clear examples, installation guidelines, how to use their modules, and data. The code is rich in comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/6)

The authors state the data set statistics in table 1, they use six datasets in total and clear download instructions are presented for FACE-3D in the implementation. With a bit of digging this is also possible for GCSS and a commented but functional link for JHU Covid. The authors describe the datasets in section 5.2 and state that Patient Claim is proprietary (Data collection is briefly stated but a lot is missing). In 5.3 and 5.4 the other datasets are specified as public. There are no citations/direct links for every dataset discussed. The authors frequently refer to the missing appendix for further details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors introduce for problem 1: 2 hyperparameters in formula 3, another in problem 2 regarding the loss functions and in problem 3 another 2. It is unclear whether these are parameters to the method. In experiment 5.2 and 5.3 they do specify the parameter R but not in 5.4. This makes the hyperparameter values very unclear. From the implementation examples they seem to be specifying only 2 values, I and R which is specified in experiment 5.3, but I is not specified in 5.2. Neither is specified in 5.4. In general this needs a lot of clarification of what parameters are actually being considered as parameters to the method for the experiment and what values are being used per experiment. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state all exerpiments are conducted with five random seeds and they report the mean and standard deviations over these. The metrics are stated with formula and citations in 5.1. They also use runtime as a metric. The evaluations are done over the entire datasets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience in data mining and online tensor factorization/completion.
