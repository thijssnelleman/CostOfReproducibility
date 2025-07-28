
## Predicting Ordinary Differential Equations with Transformers
Sören Becker, Michal Klein, Alexander Neitz, Giambattista Parascandolo, Niki Kilbertus
Keywords: 
ICML/2023/Proceedings/23844 - Predicting Ordinary Differential Equations with Transformers.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state their implementation is available online (https://github.com/soerenab/nsode23). The link gives a 404. Figure 1 summarises the method. They provide a technical detail in footnote 3. They also provide some citations to used packages in the references. They also list an opensource reference table in appendix G with citations/URLs.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/3)

The authors use benchmarks functions in 4.1: functions which they define in 4.1 (classic), functions they manually curated and summarise (table 7), and one they generate based on the previous. This generated data set is not available (implementation link not working). The distribution of the datasets are given in figure 5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors list the hyperparameter values in A.3. A full overview of considered parameters is not given. Acuiqisiton is noted as 'empirically' but no budget is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are stated in 4.3. The evaluations are on the specified test data sets. Results are per configuration/parameter setting. No aggregation/variation applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise with transformers and ordinary differential equation prediction.
