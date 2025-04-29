
## Measuring Fairness Under Unawareness of Sensitive Attributes: A Quantification-Based Approach
Alessandro Fabris, Andrea Esuli, Alejandro Moreo, Fabrizio Sebastiani
Keywords: 
JAIR/2023/Proceedings/14033 - Measuring Fairness Under Unawareness of Sensitive Attributes: A Quantification-Based Approach.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state a link to their implementation in the introduction (https://github.com/alessandro-fabris/ql4facct). There is no readme or installation notes. Code can use more comments. Pseudo code on page 1136.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use Adult, COMPAS and CreditCard dataset. They are described, cited, and linked in 5.2 and are also present in the implementation. Statistics in table 3.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

No (hyper) parameters discussed in the paper, only a parameter α which they set to 0.5 in a theoretical analysis.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors present the results with boxplots over estimation error. They also present the results in table format with MAE, MSE, and P(AE) (explained below the table) in table 4. The variance/aggregation are not explained. The authors split each data set 5 times randomly, equally in to training/auxiliary and test set. Results are presented on the teste set (d3)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on fairness.
