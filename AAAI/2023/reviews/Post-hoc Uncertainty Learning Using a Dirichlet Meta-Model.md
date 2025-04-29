
## Post-hoc Uncertainty Learning Using a Dirichlet Meta-Model
Maohao Shen, Yuheng Bu, Prasanna Sattigeri, Soumya Ghosh, Subhro Das, Gregory Wornell
Keywords: ML: Calibration & Uncertainty Quantification
AAAI/2023/Proceedings/26167 - Post-hoc Uncertainty Learning Using a Dirichlet Meta-Model.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

No implementation source can be found. The authors state more implementation details are present in the appendix but these can not be found (AAAI limitations). A design of the meta model structure, a detailed example is given. However no clarification on how it was implemented, making it extremely costly to re-implement the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(8/8)

The authors use three open source benchmark data sets for one task, and five other (seemingly open) benchmark data sets for the other task. However citations seem to be missing which makes it a bit more difficult to verify. No statistics or other details are given on the data sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors introduce a hyperparameter on their method. No details on used settings are given. The authors do provide an ablation study on their method. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors describe the baselines and datasets and how they will be evaluated, and introduce the metrics they will use for it. They state the results are averaged over 5 random runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The method requries a good understanding on meta learning. The lack of examples through implementation make it less accessible.
