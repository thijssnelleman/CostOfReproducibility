## Rethinking the Expressive Power of GNNs via Graph Biconnectivity
Bohang Zhang, Shengjie Luo, Liwei Wang, Di He
Keywords: 
Award: Outstanding Paper Award
ICLR/2023/Proceedings/576 - Rethinking the Expressive Power of GNNs via Graph Biconnectivity.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in section 5 (https://github.com/lsj2408/Graphormer-GD). In the readme the authors provide an overview of the method how to install the code with dependencies, and a section called training, which seems incomplete, and contact details to the authors. The code has good comments. Structure is large and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use two synthetic tasks in section 5, which they describe and provide code for in the implementation, as well as ZINC for which they provide a citation and a brief description. Download link is available in the implementation as is fetched automatically there when using the code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Hyperparameters are discussed in the appendix F.1. in text. Acquisition not specified. There is a semi structured file available in the implementation ('hardcoded' variables in an .sh file).

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure accuracy on the synthetic task, presented with average over 5 different seeds and MAE over four different seeds on the ZINC test set. The variation is not clarified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
