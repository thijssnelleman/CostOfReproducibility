
## Sparse NMF with Archetypal Regularization: Computational and Robustness Properties
Kayhan Behdin, Rahul Mazumder
Keywords: 
JMLR/2024/Proceedings/210233 - Sparse NMF with Archetypal Regularization: Computational and Robustness Properties.pdf
Project URL: https://github.com/kayhanbehdin/SparseAA

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation on JMLR website (https://github.com/kayhanbehdin/SparseAA) and on footnote 3. The readme is a bit chaotic, but they refer for a demo to a file. No installation notes. Code requires more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

In section 5.1 the authors use synthetic data and specify the generation process with parameters. Data generators are provided. More details in appendix E.1. In 5.2. they use the Face Data set and provide a citation and detailed descriptions but no link. In 5.3 the Cancer Gene Expression Example with the same information. In 5.4 with Indian Pines dataset (direct link given for this in the references). 5.5. scene categorization dataset. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

In section 4.4 the authors state three tuning parameters (k, l and λ) and describe them. The values are given per experiment and some are varied for ablation studies.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure validation loss, robustness, runtime and various other metrics. Not each is clear. Results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on non convex optimisation and nonnegative matrix factorization.
