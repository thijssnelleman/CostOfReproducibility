
## A Metric Space for Point Process Excitations
Myrl G. Marmarelis, Greg Ver Steeg, Aram Galstyan
Keywords: 
JAIR/2022/Proceedings/13610 - A Metric Space for Point Process Excitations.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/3)

The authors conduct experiments on synthetic data in 3.1, and describe the process with the parameter values but very briefly and the implementation is not given. In 3.2 the authors conduct real-world experiments on a COV-19 dataset (described, citation given with link but statistics are few), and options marked which is also described and statistics are given but no link/citation and does not seem to be public.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors state they try two values for m 'and a handful of choices for hyperparameter epsilon'. No other details given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors simulated 20 trials per experiments and present the results with mean and standard deviation on the test and train set with log likelihoods over various dataset sizes (n and N). In figure 2 they show the train/test log likelihoods as a gap between train and test as boxplots. The same is conducted for the other datasets. The authors describe the test split for options market, Covid 19, but not for synthetic data.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on multivariate hawkes processes. 
