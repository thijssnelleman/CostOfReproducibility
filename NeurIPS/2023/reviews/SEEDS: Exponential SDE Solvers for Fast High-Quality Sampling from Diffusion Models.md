
## SEEDS: Exponential SDE Solvers for Fast High-Quality Sampling from Diffusion Models
Martin Gonzalez, Nelson Fernandez Pinto, Thuy Tran, elies Gherbi, Hatem Hajri, Nader Masmoudi
Keywords: 
NeurIPS/2023/Proceedings/71474 - SEEDS: Exponential SDE Solvers for Fast High-Quality Sampling from Diffusion Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors link their implementation in the abstract (https://github.com/nfsrules/SEEDS). In the readme they state an overview on the method, installation requirements and that details on running the code are coming soon. The code needs an index and more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/4)

The authors use CIFAR-10, CelebA-64, FFHQ-64 and ImageNet-64 in their experiments. No links, citations, descriptions or statitstics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors discuss 4 hyperparameters in appendix F and specify the value of one (Schurn = 0). The pseudo code algorithm 2-4 does seem to take in various parameters. Values and parameters unclear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Metrics are FID (acronym written out but not explained) and NFE (formula given in D.4.). Results are over single runs. Train/test set not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on Solvers for diffusion models.
