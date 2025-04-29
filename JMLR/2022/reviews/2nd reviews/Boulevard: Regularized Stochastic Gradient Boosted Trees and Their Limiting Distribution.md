## Boulevard: Regularized Stochastic Gradient Boosted Trees and Their Limiting Distribution
Yichen Zhou, Giles Hooker
Keywords: 
JMLR/2022/Proceedings/210078 - Boulevard: Regularized Stochastic Gradient Boosted Trees and Their Limiting Distribution.pdf
Project URL: https://github.com/siriuz42/boulevard

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present their implementation online (https://github.com/siriuz42/boulevard.git). There are no installation instructions or version control info (1). there are as good as no comments (1) 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/6)

They only state "_on both simulated and real world data._" later they mention "function (1) " and "function (2" which could refer to the formulae labelled as 1 or 3 or the functions in the 6.1 (lets assume the latter) These are just functions and not data. "real world" datasets are metnioned in the figures, but not in the text. There are 4. threre is a citation, +1 no description, +1 no statistics so all the above are true. +3. The simulated functions are simple and do not need more explanation I think.

### Configuration
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

hyper parameters are introduced informally in the text +2. Parameters are specified  in a table in the appendix, but not justified +1. MSE is used but never introducesd. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

MSE is used but never introducesd.  therefore it is also not fully clear what is being measured. +0 -> MSE is standard. clear what results are on test and what on train. Not clear how the data is split +2. aggregated over 5-fold cross validation 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Things are not fully straightforward from reading the text. There are many different theories to understand and the paper stools on a limiting theory that is hard to follow. 
