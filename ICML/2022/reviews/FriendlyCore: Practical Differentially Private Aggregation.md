
## FriendlyCore: Practical Differentially Private Aggregation
Eliad Tsfadia, Edith Cohen, Haim Kaplan, Yishay Mansour, Uri Stemmer
Keywords: 
ICML/2022/Proceedings/16323 - FriendlyCore: Practical Differentially Private Aggregation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state pseudo code on their method in algorithm 4.1. and 5.3. Implementations are not given, except links to implementations of comparison methods they used for their evaluation. They state in 6.1. their method was implemented in Python. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors generate a data set and state the distribution in 6.1. The code for the generator is available online and directly linked. The parameter (n) is specified per experiment.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the privacy parameter values in section 6, the main parameters stated in their pseudo code. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state their averaging and variance in appendix E.1 including repition strategy. No train/test split applicable. The 'metric' is L2 error in figure 4.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience with clustering and data privatisation.
