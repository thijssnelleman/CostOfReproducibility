
## On Efficient and Scalable Computation of the Nonparametric Maximum Likelihood Estimator in Mixture Models
Yangjing Zhang, Ying Cui, Bodhisattva Sen, Kim-Chuan Toh
Keywords: 
JMLR/2024/Proceedings/221120 - On Efficient and Scalable Computation of the Nonparametric Maximum Likelihood Estimator in Mixture Models.pdf
Project URL: https://github.com/YangjingZhang/Dual-ALM-for-NPMLE

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation on the JMLR website (https://github.com/YangjingZhang/Dual-ALM-for-NPMLE) as well as in footnote 2. In the readme they briefly overview three files. No installation instructions. Code needs more comments. Implementation details are summarised in section 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use synthetic data for their experiments as well as two astronomy datasets (Gaia-TGAS and APOGEE with citations). The two datasets are well described but only briefly with statistics and no links given. For the synthetic data they provide the formulae and distributions as well as the parameters and code is available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the parameters of the methods in algorithm 1 and 2 and their values in appendix C. They motivate their choices based on theory/analysis.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results averaged over 10 replications. The metrics are defined in the caption of table 2. No variance, no data split.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise of nonparametric estimator and algorithmic theory.
