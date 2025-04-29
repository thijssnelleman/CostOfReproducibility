
## Additive smoothing error in backward variational inference for general state-space models
Mathis Chagneux, Elisabeth Gassiat, Pierre Gloaguen, Sylvain Le Corff
Keywords: 
JMLR/2024/Proceedings/221392 - Additive smoothing error in backward variational inference for general state-space models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state a library and framework (Haiku, JAX) in the appendix. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/2)

The authors use two types of synthetic data (formulae) and provide formulas and descriptions/citations for each of them. No implementation given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Various parameter values are named in section 4, but an overview is missing. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The experiments are presented over 50 independent replicates, with the mean and standard deviation. Data split not applicable. Metrics are error additive/marginal. In figure 2 they use 10 independent replicates instead. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on variational inference and state-space models.
