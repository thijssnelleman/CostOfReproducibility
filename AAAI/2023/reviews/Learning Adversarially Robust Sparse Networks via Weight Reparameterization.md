
## Learning Adversarially Robust Sparse Networks via Weight Reparameterization
Chenhao Li, Qiang Qiu, Zhibin Zhang, Jiafeng Guo, Xueqi Cheng
Keywords: ML: Adversarial Learning & Robustness, CV: Adversarial Attacks & Robustness, ML: Learning on the Edge & Model Compression
AAAI/2023/Proceedings/26027 - Learning Adversarially Robust Sparse Networks via Weight Reparameterization.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their implementation (https://github.com/UCAS-LCH/Twin-Rep). The readme is basically empty. The code has very few comments. They do provide a a data loader and clear entry points and some explanation is present in the argument parsers. In general this code could use instructions on requirements to get it to run, how to use which script, comments and details on how the data sets should be presented (They seem to be auto-downloaded, but with one sentence in the readme this could be clarified). An algorithm pipeline (pseudo code) is presented in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use two public data sets and cite them in their paper. Statistics are missing, but could be found by following the citation. The data sets do have data loaders in the implementations but there are no instructions on how they should be downloaded / presented so this would have to be figured out for the comparability.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Default hyperparameter values can be found in the train script of the implementation. Details on these values are also provided in the paper. How these values were acquired is unclear. The authors state the HP value for each setting is the same.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors extensively document their attacking settings, which seem all to be single model evaluations. Details could easily be extracted/verified with the implementation documentation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The independent investigators would have to have decent expertise regarding robustness and adversarial attacks.
