
## ALMA: Alternating Minimization Algorithm for Clustering Mixture Multilayer Network
Xing Fan, Marianna Pensky, Feng Yu, Teng Zhang
Keywords: 
JMLR/2022/Proceedings/210182 - ALMA: Alternating Minimization Algorithm for Clustering Mixture Multilayer Network.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors evaluate on simulations in 5.3 and provide details/parameter values but no implementation, in 5.4 the authors use worldwide food trading networks and airline flight networks, provide citations and direct links, write descriptions but statistics are a bit lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide pseudo code on their method in algorithm 1 and 2. Their own method only has semantic parameters which are specified by the problem setting. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the method over various values of n and p and measure the misclassification error over 100 independent runs and present the average with boxplots. In table 2 they report the MSE over the datasets for various values of M and K, there is not data split reported so it seems to be on the entire dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on clustering in mutlilayer networks.
