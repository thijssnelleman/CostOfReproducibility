
## Gaussian Mixture Variational Autoencoder with Contrastive Learning for Multi-Label Classification
Junwen Bai, Shufeng Kong, Carla Gomes
Keywords: 
ICML/2022/Proceedings/16865 - Gaussian Mixture Variational Autoencoder with Contrastive Learning for Multi-Label Classification.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/JunwenBai/c-gmvae). In the readme they state an overvie of the method, where to find the example dataset, installation instructions, how to run the training and testing scripts, and a link to a related repository. The code has an acceptable amount of comments. The repository structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(9/9)

The authors use 9 data sets and provide statistics in table 4. Citations are provided in 4.1. A direct link is in footnote 2. Descriptions are a bit too brief.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The architecture is stated in 4.3 and remark that 'no complex architectures are needed' for their method. Three parameters are set 'by default' (How were these selected?). The authors state they apply grid search for three other parameters. The authors provide more details per dataset in B.1. The grids for the search are also specified. Only the acquisition of a few values is unclear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use F1 scores and hamming accuracy and precision@1 (All standard). They present the results as averages over three seeds. The data split is 80/10/10 for each.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in VAE and contrastive learning.
