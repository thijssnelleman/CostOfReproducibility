
## End-to-end Differentiable Clustering with Associative Memories
Bishwajit Saha, Dmitry Krotov, Mohammed Zaki, Parikshit Ram
Keywords: 
ICML/2023/Proceedings/23967 - End-to-end Differentiable Clustering with Associative Memories.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/bsaha205/clam). In the readme they state installation instructions, where the data can be found, what the main entry points is and how parameters ca nbe modified and where the output can be found. The code is a bit noisy with a lot of unusefull comments. Structure is small and easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(10/10)

The authors evaluate their method on 10 datasets. All the data is available or directly linked in the implementation docs. A statistical summary is available in appendix A.1. with citations.  More direct links available in the appendix. Descriptions on the dataset tasks are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The author ssummarise the HPs and their values in appendix table 5, where they define the grids for optimisation and the selected parameters in table 6. There is also a file in the implemntation summarising this. The authors do not state the strategy for the search.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state the evaluation metrics used in appendix A.2. with full definitions and citations. The results are signle run/model. There are no specifications regarding data splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on clustering and associative memory models.
