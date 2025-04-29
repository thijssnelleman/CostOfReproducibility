
## Partial Order in Chaos: Consensus on Feature Attributions in the Rashomon Set
Gabriel Laberge, Yann Pequignot, Alexandre Mathieu, Foutse Khomh, Mario Marchand
Keywords: 
JMLR/2023/Proceedings/230149 - Partial Order in Chaos: Consensus on Feature Attributions in the Rashomon Set.pdf
Project URL: https://github.com/gablabc/Partial_Order_in_Chaos

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide an implementation link on the JMLR website (https://github.com/gablabc/Partial_Order_in_Chaos) as well as in footnote 1. In the readme they introduce the method, show some results, and indicate the structure of the repository. There is an installation file (environment.yml) available. Comments are pretty good.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use the kaggle housing problem dataset in 5.3 and provide a direct link. The dataset is described there and in appendix C.1. In 6.3. the authors use the ProPublica dataset and explain it extensively with citations. In 7.3 they discuss the Adult-Income dataset with direct link description and high level statistics. Datasets are also included in the implementation. More detailed statistics would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state hyperparameter tuning in 7.3. and that is was conducted over 5-fold cross validation. HP γ is defined in 6.3 and in 5.3 HP k and 4 others that are also optimised through CV. Real details and their selected values are not clear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use 5-fold cross validation and present the results as RMSE on the train and test set, state for Kaggle they submit predictions to the Kaggle website (static test set), for COMPAS its only stated the ratio of splitting but now how, same for adult income.The authors also measure misclassification rate and mean cardinality. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries experitse on feature attribution and rashomon set.
