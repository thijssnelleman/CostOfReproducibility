
## Online Combinatorial Optimization with Group Fairness Constraints
Negin Golrezaei, Rad Niazadeh, Kumar Kshitij Patel, Fransisca Susan
Keywords: AI Ethics, Trust, Fairness: ETF: Fairness and diversity, Constraint Satisfaction and Optimization: CSO: Mixed discrete and continuous optimization, Machine Learning: ML: Online learning, Machine Learning: ML: Optimization
Award: Distinguished Paper Award
IJCAI/2024/Proceedings/0044 - Online Combinatorial Optimization with Group Fairness Constraints.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors do not provide implementation documentation. The authors describe their implementation extensively in the fourth paragraph of section 4. They provide the citations on methods/algorithms/functions used and their values, and refer to the full version of the paper for more details (which they link). Pseudo code is given in algorithm 1, and a second one in the extended version. Practical details on the code are missing. However, the authors state in section five their framework 'is easy to state and implement'. Yet, without practical details/examples this will still be a serious effort.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors do a case study with a public dataset (stated in the extended version) and provide a citation on it. The task is described in the extended version with statistics and data structure. A direct link is missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state various algorithm parameters in their pseudo code (algorithm 1,2) and they discuss the values of algorithm 1 in section 4 paragraph 2 where they present a grid of values being considered. The authors analyse the fairness threshold in figure 2, and more parameter values are discussed in the following paragraph. It will take some carefull reading to extract all values being discussed/presented, but in general the documentation looks complete. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they average the performance over 50 runs in their experiments. The authors state the formula for their metric market share. In figure 2b they analyse two parameters against eachother. In figure 1 they analyse cumulative regret as discussed in algorithm 1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires deep experience with combinatorial optimization, online/offline learning and recommender systems, especialyl to grasp the problem formulation. However examples are given and the pseudo code is extensive yet the absence of their implementation makes it somewhat more difficult as it would serve as a good example to guide the investigator through their method.
