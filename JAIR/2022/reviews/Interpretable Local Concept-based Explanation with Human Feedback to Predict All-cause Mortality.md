
## Interpretable Local Concept-based Explanation with Human Feedback to Predict All-cause Mortality
Radwa EL Shawi, Mouaz H. Al-Mallah
Keywords: 
JAIR/2022/Proceedings/14019 - Interpretable Local Concept-based Explanation with Human Feedback to Predict All-cause Mortality.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use the Henry Ford FIT dataset and describe it in 4.1. with citations. Statistics are okay. No link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

Not discussed (They use RF and SVM which are configurable)

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors split the data 60/20/20 (4.2.). In table 1 they present the results on the testing dataset as accuracy with std deviation. In figure 3 they plot the accuracy against randomly selected features (features described in 4.2.). The authors measure F1 score averaged over 50 runs in figure 4 but don't specify which set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on explainable AI with human feedback.
