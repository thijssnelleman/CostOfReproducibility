
## IMO^3: Interactive Multi-Objective Off-Policy Optimization
Nan Wang, Hongning Wang, Maryam Karimzadehgan, Branislav Kveton, Craig Boutilier
Keywords: Machine Learning: Experimental Methodology, Machine Learning: Optimisation, Uncertainty in AI: Decision and Utility Theory, Knowledge Representation and Reasoning: Preference Modelling and Preference-Based Reasoning, Humans and AI: Human-AI Collaboration
IJCAI/2022/Proceedings/0489 - IMO^3: Interactive Multi-Objective Off-Policy Optimization.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state in the extended version of the paper (which they link) that the implementations used for the experiments will be made public after publication, but no link can be found. The authors present pseudo code on the method in algorithm 1.s

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors evaluate the method on four MOO problems in section 6. They state a description on each with citations and key statistics. They expand on each in the appendix of the extended version of the paper. No direct links to the data given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the parameter values of the pseudo code in section 6.2. They experiment with different estimators in the appendix. The authors evaluated over the log data and budget in the experiments, fixing the other to a specified value. For the L parameter  no acquisition is stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure simple regret and evaluate each experiment averaged over 5 runs in each experiment. They define simple regret in section 3 with a citation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience with RL, MOO including practical experience as implementation details are missing.
