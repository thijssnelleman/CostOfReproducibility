
## Recovering the Propensity Score from Biased Positive Unlabeled Data
Walter Gerych, Thomas Hartvigsen, Luke Buquicchio, Emmanuel Agu, Elke Rundensteiner
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20624 - Recovering the Propensity Score from Biased Positive Unlabeled Data.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors refer to publicly available code they use for part of their implementation. No other details are given regarding the implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The author use six benchmark data sets from a public repository and provide citations on them, likeise they use two more real-world data sets. There is a motivation regarding the data set selection which reveals some of its properties, but real details are missing. They do refer to the supplementary materials but these are not present/linked.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Based on information presented in the paper, the method is seemingly parameter-free but this needs some verification. Without the implementation this is slightly more difficult to verify.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the splitting of the data for training/testing and that its randomised and repeated 10 fold for each experiment. They measure the propensity score which is discussed to great length in the paper. They also use mean absolute error, which is straightforward.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a lot of expertise regarding data and statistics.
