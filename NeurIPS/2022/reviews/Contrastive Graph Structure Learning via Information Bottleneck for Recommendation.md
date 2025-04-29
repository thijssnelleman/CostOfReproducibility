
## Contrastive Graph Structure Learning via Information Bottleneck for Recommendation
Chunyu Wei, Jian Liang, Di Liu, Fei Wang
Keywords: 
NeurIPS/2022/Proceedings/54116 - Contrastive Graph Structure Learning via Information Bottleneck for Recommendation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 2 (https://github.com/weicy15/CGI). In the readme they state installation instruction, how to prepare the data, how to train models, and how to evaluate. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors details the datasets with a descriptions, statistics, citations and direct links ion appendix F. Only the Douban dataset does not have a link but does seem to be included in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors introduce a couple of HPs in section 4. Their values are stated informally in section 5.1. The authors seem to imply they are empirically optimised ('carefully tuned') but its not completely clear. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics with formulae/citations in sec 5.1. and the appendix G. Data split defined in 5.1. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on graph structure learning and recommender systems.
