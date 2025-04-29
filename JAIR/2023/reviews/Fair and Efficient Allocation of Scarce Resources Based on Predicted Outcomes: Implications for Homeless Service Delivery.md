
## Fair and Efficient Allocation of Scarce Resources Based on Predicted Outcomes: Implications for Homeless Service Delivery
Amanda R. Kube, Sanmay Das, Patrick J. Fowler
Keywords: 
JAIR/2023/Proceedings/12847 - Fair and Efficient Allocation of Scarce Resources Based on Predicted Outcomes: Implications for Homeless Service Delivery.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

Implementation not given but they state they used the R package BayesTree and provide a citation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

In 4.2 the authors use homelessness data and provide a link to the dataset. They describe the dataset in detail and extensive statistics in table 5. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameters of the methods used in 4.1 and in case of BART some of the values were acquired. For other methods they state they were chosen because they are default/common (fine as these are not their own methods). No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors measure AUC, misclassification error, precision, recall and calibration (explained). They use 10-fold cross validation but aggregation is not specified. For table 3 and 4 its not specified on which dataset they produce the results on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on fairness in ML
