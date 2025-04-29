
## Provable Advantage of Curriculum Learning on Parity Targets with Mixed Inputs
Emmanuel Abbe, Elisabetta Cornacchia, Aryo Lotfi
Keywords: 
NeurIPS/2023/Proceedings/72605 - Provable Advantage of Curriculum Learning on Parity Targets with Mixed Inputs.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 4 (https://github.com/aryol/parity-curriculum). In the readme they index the files in the repository. No installation instructions. Has oaky comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use synthetic data, the generators are provided in the implementation but are not really described in the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Model architectures and HP values are stated in sec 5. They are also provided in the code (hardcoded). In the appendix HPO is stated but not described.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present their results with 10 random seeds and 95% CI as variance. Aggregation not specified. Results are over training. Metric is accuracy.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on curriculum learning.
