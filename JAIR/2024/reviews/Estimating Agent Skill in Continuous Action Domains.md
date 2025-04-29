
## Estimating Agent Skill in Continuous Action Domains
Christopher Archibald, Delma Nieves-Rivera
Keywords: 
JAIR/2024/Proceedings/15326 - Estimating Agent Skill in Continuous Action Domains.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. The authors state they use a python package in section 10.1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use 'Darts' simulation in section 5 and 9.1. and describe it in 8.1. but do not provide an implementation. In section 10 they use a baseball simulation and describe it, and provide a link to the data in 10.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

In section 1.1.3 the authors discuss a delta parameter. Parameter β is introduced in eq. 3 and described. Its values are stated in text and varied across experiments. It is not clear what the authors consider exactly as parameters and how values are acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use MSE as a metric, computes across all experiments over the number of observations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on agent skill estimation.
