
## Learning Provably Robust Estimators for Inverse Problems via Jittering
Anselm Krainovic, Mahdi Soltanolkotabi, Reinhard Heckel
Keywords: 
NeurIPS/2023/Proceedings/70848 - Learning Provably Robust Estimators for Inverse Problems via Jittering.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/MLI-lab/robust_reconstructors_via_jittering). In the readme they state the method, list the contents, state how to install, link the datasets, how to run the code, an overview on the pipeline, and code acknowledgements. The code needs more comments. The structure is quite large but still overseeable (directory depth is not too deep). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors provide download links for FastMRI and ImageNet in the implementation. Only FastMRI is used. Its described in 4.1 but statistics are a bit lacking. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the network architecture in 4.1. The hyperparameter values are stated at the end. Configuration files are given in the implementation for structured overview. The authors state how the sigma parameter was selected in appendix D.4. and visualise the search in figure 3, budget not entirely clear. This is the only parameter they describe but more are implied. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The evaluation metrics are described in 4.1. Data split is done by random sampling and split ratio is defined. The metrics are not completely clear. No variation/aggregation applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in robustness.
