
## On Tail Decay Rate Estimation of Loss Function Distributions
Etrit Haxholli, Marco Lorenzi
Keywords: 
JMLR/2024/Proceedings/220846 - On Tail Decay Rate Estimation of Loss Function Distributions.pdf
Project URL: https://github.com/ehaxholli/CTE

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website (https://github.com/ehaxholli/CTE). In the readme they state the purpose of the repository. The code is seperated per section of the paper and is easy to oversee. There are no installation instructions. Comments are good.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use simulated data in 5.1 and 5.2 (formulae and parameters provided) and in 5.3 they use a dataset from UCR which they cite and provide a direct link to. Descriptions and statistics lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The only parameter the authors seemingly consider is the estimator (Pickands or DEdH) which they mainly use Pickands for but also present results in the appendix for DEdH and in figure 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate shape parameter (problem specific) and variation is repition (p and n) in the algorithm. They present the results with mean and 3 std devs. Figure 5 is average + std dev over 200 runs and measures MSE.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on loss function distributions.
