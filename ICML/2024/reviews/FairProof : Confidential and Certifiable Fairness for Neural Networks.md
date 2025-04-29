
## FairProof : Confidential and Certifiable Fairness for Neural Networks
Chhavi Yadav, Amrita Roy Chowdhury, Dan Boneh, Kamalika Chaudhuri
Keywords: 
ICML/2024/Proceedings/34587 - FairProof : Confidential and Certifiable Fairness for Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/infinite-pursuits/FairProof). In the readme they state a brief description on some code files. The code could use more comments. There are no installation instructions. Pseudo code is available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use three benchmark datasets, describe them with citations. No statistics given. No direct links provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method is parameter free. They do provide HPs on the networks that will be used as input for the method in section 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure the frequency of the fairness parameter epsilon with mean and standard deviation. They also measure time as a metric. The results are per model.  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on fairness and verification on neural networks.
