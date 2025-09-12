
## Unbiased Active Semi-supervised Binary Classification Models
JooChul Lee, Weidong Ma, Ziyang Wang
Keywords: Machine Learning: ML: Active learning, Machine Learning: ML: Regression, Machine Learning: ML: Semi-supervised learning
IJCAI/2024/Proceedings/0485 - Unbiased Active Semi-supervised Binary Classification Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide a link to the codes used for the numerical studies (https://github.com/IJCAI-24/ActiveSemiPrediction). The repository lacks a readme and the code has very few comments. In general it will take some serious engineering to understand how the code works exactly to use it as input for re-implementation. There are no overviews presented in the paper that could help here.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors use synhetic data in section 6.1 and explain how it was generated, and the code for it could supposedly be found in the repository for it. Futhermore they use for public data sets, provide the direct links, a short description and key statistics. No citation is provided on the data set, but the direct links make up for that in this case.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The presented method is seemingly parameterfree, based on the pseudo code presented.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state in figure 2 the metrics used and the evaluation procedure. However to fully understand the experiments serious domain knowledge is required.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The presented method is complex and requires alot of domain knowledge to grasp. This is worsened by the lack of documentation in the implementation.
