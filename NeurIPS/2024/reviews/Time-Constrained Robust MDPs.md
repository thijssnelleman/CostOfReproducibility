
## Time-Constrained Robust MDPs
Adil Zouitine, David Bertoin, Pierre Clavier, Matthieu Geist, Emmanuel Rachelson
Keywords: 
NeurIPS/2024/Proceedings/95448 - Time-Constrained Robust MDPs.pdf
Project URL: https://openreview.net/attachment?id=NKpPnb3YNg&name=supplementary_material

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their implementation as supplementary material on open review (https://openreview.net/attachment?id=NKpPnb3YNg&name=supplementary_material). In the implementation are two directories with implementations. TCMDP has a readme with installation instructions and an overview of the structure, and how to run the code. RRLS does not have this. Its unclear what the code of the authors is and what is sourced from elsewhere. Some pieces of code have good comments others do not at all.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use 5 public environments included in their implementation installation. The source of this is cited but the tasks/environments are not explained. There is no specification of environment parameters.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters are given in the appendix in table 5 and 6 per method. No acquisition given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

In caption of table 1 the authors state they present the results averaged over 10 seeds for each method. Variation not explained. The metric is episode reward. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on MDPs and RL.
