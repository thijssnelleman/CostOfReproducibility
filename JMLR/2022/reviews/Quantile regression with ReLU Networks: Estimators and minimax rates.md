
## Quantile regression with ReLU Networks: Estimators and minimax rates
Oscar Hernan Madrid Padilla, Wesley Tansey, Yanzhen Chen
Keywords: 
JMLR/2022/Proceedings/210309 - Quantile regression with ReLU Networks: Estimators and minimax rates.pdf
Project URL: https://github.com/tansey/quantile-regression

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state a link for the implementation in the abstract and on the JMLR website (https://github.com/tansey/quantile-regression). In the readme they state where what specifc part of the implementation can be found and the required libraries but also 'usualy dependencies apply' and versions are unclear. Code requires more/better comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors state they use both synthetic and real data. For the synthetic data they explain and state the formulas with parameters for each scenario. Generator code available. Real-data experiments not found.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors describe the architectures and (hyper)parameter values in 4.1 informally and they can be found in the implementation. Acquisition not explained. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metric is MSe (formula given) over 25 monte carlo simulations for two synthetic mutlivariate benchmarks, squarred error over 25 trials for univariate. No data split used.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on on DNNs and quantile regression.
