
## Localized Debiased Machine Learning: Efficient Inference on Quantile Treatment Effects and Beyond
Nathan Kallus, Xiaojie Mao, Masatoshi Uehara
Keywords: 
JMLR/2024/Proceedings/230661 - Localized Debiased Machine Learning: Efficient Inference on Quantile Treatment Effects and Beyond.pdf
Project URL: https://github.com/CausalML/LocalizedDebiasedMachineLearning

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to the implementation in the JMLR website and in section 6 (https://github.com/CausalML/LocalizedDebiasedMachineLearning). In the readme they refer to which pieces of code are responsible for which result figures/tables and where the dataset can be found with link. No installation instructions. Code has good comments for one file but almost none for the other 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors provide a link to dataset in the implementation and code for simulations. They describe the simulator in 6.1. In 6.2. they conduct an experiment on a dataset which they cite and provide online a link to. The data set is well described but statistics are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Hyperparameters are stated informally in sec 6.2 and 6.3 (K and nuisance estimators). They evaluate them over different configurations. No full overview on the HPs.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

Metrics used are MSE and coverage. They evaluate over 250 replications and report with +/- std error. Results are also displayed for 25/5/65 quantiles. No data set split mentioned.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on ML causal inference.
