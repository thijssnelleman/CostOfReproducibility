
## NoiseGrad — Enhancing Explanations by Introducing Stochasticity to Model Weights
Kirill Bykov, Anna Hedström, Shinichi Nakajima, Marina M.-C. Höhne
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20561 - NoiseGrad — Enhancing Explanations by Introducing Stochasticity to Model Weights.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not provide a link to their own implementation, but do provide direct links of two libraries they use in their method. No other details are provided on the implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/3)

The authors construct a dataset from two public well known data sets. This constructed data set is seemingly not published and its not clear how much effort is needed for reconstruction. They use two more public data sets for evaluation and provide a short description on them. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The model architectures are in the (missing) appendix. The authors state that their method has an 'automatic hyperparameter choice' and that it does not require hyperparameter tuning. With the presence of the appendix or implementation docs, this would probably be 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors explain the metrics of the procedure extensively, but refer for data set details (train/test split, processing) to the non existent appendix (AAAI limitations). With the presence of the appendix this would probably be 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method requires experience with explainable black-box ML. 
