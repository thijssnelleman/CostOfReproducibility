
## Fast and Regret Optimal Best Arm Identification: Fundamental Limits and Low-Complexity Algorithms
Qining Zhang, Lei Ying
Keywords: 
NeurIPS/2023/Proceedings/71286 - Fast and Regret Optimal Best Arm Identification: Fundamental Limits and Low-Complexity Algorithms.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their code in the supplementary material (https://openreview.net/attachment?id=Yc9bqbnrbs&name=supplementary_material). No readme given. The code has very few comments. Although the size is not very large, the structure is not intuitive cryptic. The code is also quite cryptic.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use simulated data and provide the parameters of the simulation in section 6. Simulator code is provided. Descriptions are too brief to easily understand. Code structure is cryptic, not helping either.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The algorithms seem parameter free but there is an exploration function and lower bound parameter needed but these are not clear and there is no discussion on the parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure regret (formula giben in sec 2) as metric over the number of rounds. Results are averaged over 10^5 iterations. Test split not applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries expertise on multi armed bandits.
