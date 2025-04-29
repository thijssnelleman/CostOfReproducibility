
## Learning Preference Models with Sparse Interactions of Criteria
Margot Herin, Patrice Perny, Nataliya Sokolovska
Keywords: Machine Learning: ML: Learning preferences or rankings, Knowledge Representation and Reasoning: KRR: Preference modelling and preference-based reasoning, Uncertainty in AI: UAI: Decision and utility theory
IJCAI/2023/Proceedings/0421 - Learning Preference Models with Sparse Interactions of Criteria.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation nor are any details on it given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state they generate data using a function with some gaussian noise. The parameters and details regarding this generation are given but does require some mathematical experience to understand. The authors also state the size of the training and test sets. The implementation of this generation is not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state the value of the regularization parameter in section 4. The smoothing parameter is also given for D-IRLS. No other details are given, and it is difficult to verify these are the only needed parameters for the method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state how the training/testing sets are generated in section 4. They state they generate 10 data sets and evaluate the average regarding time, in table 2 they evaluate the test error, a metric explained in section 3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on the complex mathematics (choquet integrals, mobius masses) used in the method. 
