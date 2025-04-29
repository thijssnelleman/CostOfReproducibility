
## Coordinated Double Machine Learning
Nitai Fingerhut, Matteo Sesia, Yaniv Romano
Keywords: 
ICML/2022/Proceedings/16849 - Coordinated Double Machine Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/nitaifingerhut/C-DML). In the readme they state which notebook comntains what and where the core of the method can be found. There is an installation file available. There are very few comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use a synthetic dataset generator for the hyperparameter tuning in 3.3. This is reused in 4.2. In 4.3. they discuss a dataset they 'borrow' and describe briefly before they discuss turning it into a semi synthetic data set. In section 5 they use a real world data set which they cite and describe. The synthetic generator is available in the implementation. No direct links and few statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors discuss training and HP tuning in 3.2 and show the result in figure 2. The budget isn't fully clear. Architecture details are given in D.1. as well as a few HP values. Overview of HPs is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate estimation errors, density (task specific) and temperature effects on ozone concentration (data specific). The authors state they use cross-validation, a method they define in their paper.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on double machine learning.
