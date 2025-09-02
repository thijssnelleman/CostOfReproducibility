## Constructing a Good Behavior Basis for Transfer using Generalized Policy Updates
Safa Alver, Doina Precup
Keywords: 
ICLR/2022/Proceedings/6493 - Constructing a Good Behavior Basis for Transfer using Generalized Policy Updates.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors state a link to an implementation for parts of their experiment in appendix B.2. which can serve as a good starting point. More details are given in appendix B regarding the implementation. Pseudo code in algorithm 1. Furthermore the authors refer to another paper's supplementary material they used as well. The linked repository does seem to contain a large part of the required code. As the authors do a theoretical analyse with a relatively simple proposed algorithm, this information significantly lowers the required effort, although a full implementation will still have to be made from these 'ingredients'.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use the 2D item collection environment, which is public and they provide a citation for it. They visualise it in figure 1 and provide more details in appendix B.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors list the hyperparameters (Of another method than their own) and their values in table 1. Their own method only takes a budget, thus acquisition not needed.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors evaluate the method over 5 runs and present the average as normalized sum of rewards.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
