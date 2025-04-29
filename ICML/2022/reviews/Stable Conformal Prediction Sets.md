
## Stable Conformal Prediction Sets
Eugene Ndiaye
Keywords: 
Award: Outstanding Paper
ICML/2022/Proceedings/78 - Stable Conformal Prediction Sets.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in section 4 (https://github.com/EugeneNdiaye/stable_conformal_prediction). In the readme they state installation requriements, and a scrip to launch to generate figures. Code can use some better comments. Structure could use some explanation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/4)

The datasets are stated per experiment (Boston, housing california, diabetes and friedman) but no details are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors fix the alpha parameter at the beginning of section 4. No motivation given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors run each evaluation with 100 repitions and present the average. Metrics are defined in sec 4. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on conformal prediction.
