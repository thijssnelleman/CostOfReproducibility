
## The Brier Score under Administrative Censoring: Problems and a Solution
Håvard Kvamme, Ørnulf Borgan
Keywords: 
JMLR/2023/Proceedings/191030 - The Brier Score under Administrative Censoring: Problems and a Solution.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the introduction and section 6 (https://github.com/havakv/pycox). In the readme they state installation instruction, links to tutorials, implemented methods, implemented metrics, included datasets and more installation instructions. The code has very good comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

In section 5 the authors conduct experiments on simulation that are detailed there with formulae and parameter (values) and implementation is available. In section 6 they use the KKBox data set (citation, description and statistics provided in section 2) and downloads automatically through the code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the architecture and hyperparameter values of their network in section 5.1 and 6. Acquisition and structured overview not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the dataset split in section 6, results are on the test set. Results are single run, metric is brier score (explained).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise onbrier score and time-to-event prediction.
