## Semi-supervised and unsupervised extreme learning machines
Gao Huang, Shiji Song, Jatinder N. D. Gupta, Cheng Wu
Keywords: Clustering, embedding, extreme learning machine (ELM), manifold regularization, semi-supervised learning, unsupervised learning
extra_reviews/2014/Proceedings/Semi-supervised and unsupervised extreme learning machines.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. Detailed pseudo code in algorithm 1-2. There are a few notes on the implementation throughout the paper but these contain little information.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(10/10)

The authors use for semi supervised G50C, COIL20, USPST datasets and describe them + statistics in table 1. They also use IRIS, WINE, SEGMENT, COIL20, USPST, YALEB, ORL with statistics in table 4. Citations provided for all. Descriptions are short and no direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

The authors specify HP details in VII A. and B. In A. they state they optimised the tradeoff parameters based on a grid using the validation set. In B. they state the lambda parameter was selector from a grid based on the clustering performance. Structured overview missing and not all values motivated. The final selected values of each grid are not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

For the semi supervised experiments the authors conduct 4 fold cross-validation (1 fold used as test each repition), which they repeat three times. For unsupervised the experiment was repeated 100 times. The authors measure clustering accuracy, runtime, testing error and the variation is standard deviation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
