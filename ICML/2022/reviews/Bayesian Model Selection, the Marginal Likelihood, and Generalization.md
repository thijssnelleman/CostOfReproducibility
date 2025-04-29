
## Bayesian Model Selection, the Marginal Likelihood, and Generalization
Sanae Lotfi, Pavel Izmailov, Gregory Benton, Micah Goldblum, Andrew Wilson
Keywords: 
Award: Outstanding Paper
ICML/2022/Proceedings/182 - Bayesian Model Selection, the Marginal Likelihood, and Generalization.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

A link is given for dataset downloading but no for their implementation. There are details on the implementation in the appendix but they do not contain practical details.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(3/3)

The authors provide a link they use for a package to do dataset downloading regarding regression tasks. In section 5 the authors use CIFAR-10 and CIFAR-100 but no details are given. They also use simulated data from a Fourier model which they describe with parameter values but no implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors conduct neural architecture search in their experiments and provide the possible values in appendix H. Not all parameters are optimised and some are just stated. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The results are on the test set in figure 4. Figure 3 are training results on the synthetic data. Some metrics require experience with the task. Data split is stated in appendix D and F.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on model selection and HP optimisation / neural architecture search.
