
## Cross-Domain Few-Shot Semantic Segmentation via Doubly Matching Transformation
Jiayi Chen, Rong Quan, Jie Qin
Keywords: Computer Vision: CV: Segmentation, Computer Vision: CV: Transfer, low-shot, semi- and un- supervised learning
IJCAI/2024/Proceedings/0071 - Cross-Domain Few-Shot Semantic Segmentation via Doubly Matching Transformation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/ChenJiayi68/DMTNet). Their readme has an introduction on the method with visualisation, how to get the data used and the general file organisation to apply the implementation to it, details on the environment requirements, training instructions, how to run tests and a download link to their trained model and a visualisation of the output. They also acknowledge and link the repositories on which theirs is based. The code is clearly documented with comments and the directory structure is easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors provide download links and instructions in the implementation docs. In section 4.1 they provide descriptions and statistics on each data set. In section 1 citations are provided on each. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors do an ablation study of finetuning their introduced parameters and show the results in table 3. They state architecture details and hyperparameter values per data set in section 4.2. No details are given on how the latter values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state in section 4.1 the metric used and that the process has been repeated for 5 runs with random seeds and aggregate by averaging. The authors state on which data set the methods are trained on and use the other data sets for testing. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The authors present a work on various subdomains in ML, requiring diverse expertise for the independent investigators. Documentation is very rich in information which lowers the cost.
