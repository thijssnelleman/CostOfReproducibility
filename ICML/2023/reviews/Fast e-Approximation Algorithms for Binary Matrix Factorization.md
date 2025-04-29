
## Fast e-Approximation Algorithms for Binary Matrix Factorization
Ameya Velingker, Maximilian Vötsch, David Woodruff, Samson Zhou
Keywords: 
ICML/2023/Proceedings/24788 - Fast e-Approximation Algorithms for Binary Matrix Factorization.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors do not share their implementation, but they do state they developed it in python and a library they used for (parts of) it. The authors provide 5 pieces of extensive pseudo code. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use two benchmark data sets for which they cite the source, provide a description and statistics on and a direct link for one of them. For the synthetic data the authors state the generation process with variables and the amount of data they generate. Code for the generator is not published.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate the methods over various values of K. The parameter epsilon is not mentioned, but it is seemingly resolved in the introduction of the experiments. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use frobenius norm error and time as metrics. The runs a singular (no repititon). No data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise with binary matrix factorization.
