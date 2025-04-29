
## The LM-Cut Heuristic Family for Optimal Numeric Planning with Simple Conditions
Ryo Kuroiwa, Alexander Shleyfman, Chiara Piacentini, Margarita P. Castro, J. Christopher Beck
Keywords: 
JAIR/2022/Proceedings/14034 - The LM-Cut Heuristic Family for Optimal Numeric Planning with Simple Conditions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state a link to their implementation in 5.6 in footnote 4 (https://github.com/Kurorororo/numeric-fast-downward) and which compiler they used. In the readme they state installation instructions, a lot of examples how to run the code, with various parameters and a link for a project page with contact details. Code has good comments, structure is overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(22/22)

The authors use subsets of datasets such as COUNTERS, SAILING, FARMLAND, GARDENING. There are very few details given on these dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors run the method under different configurations/heuristics described in 5.2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure coverage (number of instances solved), time score (formula given) and number of states expanded. The time limit is set to 30 minutes. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on numeric planning and SAT solving.
