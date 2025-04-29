
## Empirical Bayesian Approaches for Robust Constraint-based Causal Discovery under Insufficient Data
Zijun Cui, Naiyu Yin, Yuru Wang, Qiang Ji
Keywords: Uncertainty in AI: Graphical Models, Uncertainty in AI: Causality, Structural Causal Models and Causal Inference
IJCAI/2022/Proceedings/0672 - Empirical Bayesian Approaches for Robust Constraint-based Causal Discovery under Insufficient Data.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors present a link to an implementation regarding (supposedly) the statistical independence test, but it gives a 404 error. No other implementation details are given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(6/6)

The authors state they used six benchmark datasets in section 4, for which they provide a direct link. The name of each dataset is given but no other details are provided such as citations, descriptions or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors present an independence test, which has probability distributions parameters theta, but not its own parameters e.g. these serve as input to the method not as configurations. However in the descriptions of formula five variable alpha zero and one are marked as hyper-parameters but they seemingly remove this on their new proposed approach in formula six. The method is thus seemingly parameter free but it needs some verification (which is difficult without the implementation).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used with details/citations in section 4 and state each experiments is repeated ten times and they present averaged performance including std of SHD. There is no notes of training/testing sets, which does make sense as the presented method does not have a training procedure. They also present independence tests on each data set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a good understanding of bayesian appraoches and independence tests.
