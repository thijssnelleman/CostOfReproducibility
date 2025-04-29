
## Levin Tree Search with Context Models
Laurent Orseau, Marcus Hutter, Levi H. S. Lelis
Keywords: Search: S: Search and machine learning, Search: S: Heuristic search
Award: Distinguished Paper
IJCAI/2023/Proceedings/0624 - Levin Tree Search with Context Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/google-deepmind/levintreesearch_cm). In the readme the authors state installation instructions, a quick start example, specific instructions on how to reproduce the papers results, details on the dependencies, and direct links to the datasets. The code base seems rather large but is rich in comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The implementation docs provide direct links to the datasets and files in the implementation. The authors state the three domains/datasets in section 6 with descriptions and citations. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameter values in section 6, and refer for details to the appendix which they link. The parameters for the method are seemingly quite complex except for the epsilon values which are simply stated but not specified how to acquire them.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate on the test sets, which are given as files in the implementation docs. The training/testing splits are specified per data set as are the training procedures. The metrics used are percentage solved, running time which are straight forward abnd length/expansion which are task specific metrics. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires a lot of previous experience in search algorithms but the method is very complete in its documentation even providing direct instructions how to achieve the presented results. This substantially lowers this cost.
