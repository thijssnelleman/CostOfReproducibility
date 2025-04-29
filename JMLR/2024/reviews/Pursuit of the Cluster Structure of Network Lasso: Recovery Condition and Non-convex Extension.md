
## Pursuit of the Cluster Structure of Network Lasso: Recovery Condition and Non-convex Extension
Shotaro Yagishita, Jun-ya Gotoh
Keywords: 
JMLR/2024/Proceedings/211190 - Pursuit of the Cluster Structure of Network Lasso: Recovery Condition and Non-convex Extension.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation but do state in what programming language it was implemented and under what OS in section 5.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(2/2)

The authors conduct experiments in 5.1 on a complete graph with 2 labels. They show the datasets in figure 2 but the generation conditions are not completely clear. In 5.2. and 5.3. they use a different synthetic problem which htey describe with parameter values. They also use real datasets from scikit learn which they give a direct link to. In general it will be quite a lot of work to reconstruct the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors present the results over various values of t and fix the value of ρ. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure the mean and standard deviation of the adjusted rand index (not defined). Splits not applicable. Variation is over the dataset. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on cluster structures. 
