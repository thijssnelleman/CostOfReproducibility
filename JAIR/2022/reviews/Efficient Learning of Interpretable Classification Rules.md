
## Efficient Learning of Interpretable Classification Rules
Bishwamittra Ghosh, Dmitry Malioutov, Kuldeep S. Meel
Keywords: 
JAIR/2022/Proceedings/13482 - Efficient Learning of Interpretable Classification Rules.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state a link to their implementation in the abstract (https://github.com/meelgroup/mlic). In the readme they state installation instructions, a documentation notebook link and some notes regarding older versions. Code could use better/more informative comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(15/15)

The authors use real world binary classification datasets from UCI, Open-ML and Kaggle (All cited / linked) and the authors state a few details on them in table 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors tune the hyperparameters during cross-fold validation, and they vary k, delta, n' and over grid search of 100 combinations. The selected values are not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors perform ten-fold cross-validation on each dataset and measure the performance as median accuracy on the test data. They also measure rule-size (3.3) and scalability in terms of instances solved over training time in seconds. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on rule learning.
