
## Post-Regularization Confidence Bands for Ordinary Differential Equations
Xiaowu Dai, Lexin Li
Keywords: 
JMLR/2024/Proceedings/220487 - Post-Regularization Confidence Bands for Ordinary Differential Equations.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors conduct simulation studies in 6.1 and 6.2. They give the formulas in 24/25 and specify the parameters below. Implementation not given. In section 7 they use two datasets which they describe and cite with various statistics. Direct links not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The pseudo code in algorithm 1 does not seem to have any input parameters but there are some optimization parameters for formula 17 and 18 which they use in the pseudo code. Its unclear what is used as they are stated in the list of parameters of appendix A.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are coverage probability and confidence band area and they present the results with 95% confidence intervals over 500 data replications. Noise variance specified per result. In figure 1 they present false discovery proprotion over various noise levels averaged over 500 replications. Metrics are explained. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on local polynomial approximentio nand ordinary differential equations.
