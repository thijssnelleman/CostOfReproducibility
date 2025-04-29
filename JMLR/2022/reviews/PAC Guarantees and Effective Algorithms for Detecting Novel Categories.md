
## PAC Guarantees and Effective Algorithms for Detecting Novel Categories
Si Liu, Risheek Garrepalli, Dan Hendrycks, Alan Fern, Debashis Mondal, Thomas G. Dietterich
Keywords: 
JMLR/2022/Proceedings/210451 - PAC Guarantees and Effective Algorithms for Detecting Novel Categories.pdf
Project URL: https://github.com/liusi2019/ocd-journal

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website and in footnote 1 (https://github.com/liusi2019/ocd-journal). In the readme they state where to find the code for which experiments, where to find the datasets, links to code they used from others. The code has good comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(9/9)

The authors use synthetic datasets for Q1 and Q2 and describe the distributions in sec 7 with probability values. Generator code provided in the notebook. Then the authors use benchmark datasets and state the names (Landsat, Opt.digits, pageb, Letter Recognition, Shuttle, Covertype, MNIST and Tiny ImageNet). The datasets are included in the implementation. No citations/descriptions/statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state pseudo code in algorithm 1 and 2 but don't specify input parameters. In the benchmark dataset experiments the authors state they train a deep NN for tiny imagenet. The authors conduct exerpiments over a varying alpha and n parameter, for the benchmark the n value is fixed and values are given per dataset. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure FPR and recall for the experiments. Variation is 95% CI. Aggregation is median, population is 100 trials for the synthetic experiments, 10-fold cross validation for benchmarks. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on anomaly detection.
