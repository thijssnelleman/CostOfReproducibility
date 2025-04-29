
## Simplifying Complex Observation Models in Continuous POMDP Planning with Probabilistic Guarantees and Practice
Idan Lev-Yehudi, Moran Barenboim, Vadim Indelman
Keywords: PRS: Planning with Markov Models (MDPs, POMDPs)
AAAI/2024/Proceedings/31749 - Simplifying Complex Observation Models in Continuous POMDP Planning with Probabilistic Guarantees and Practice.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide no source for their implementation. However, there is an implementation section where the authors extensively describe the setting and choices made for evaluating their method. However, the absence of any source means each detail described would have to be implemented from scratch without any example implementation to use. Furthermore, the authors provide no details in what language nor what libraries were used. Thus independent investegators would have to explore the citations for other details. The authors do provide two illustrations of their method, but no architecture/framework schematic is to be found nor is pseudo code present. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/1)

The authors describe the simulation setting in which they evaluate their method. Its described extensively with a large diagram, however no source to it can be found. Thus independent investigators would either have to reimplement the simulation or find a similar one. Defending comparison would be accesible due to the many details given on the state/action space.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors describe various hyperparameter descions and evaluations in their implementation of bounds documentation, and refer to the supplementary material for more details. No supplementary material is present in the paper however, due to AAAI limitations. As the implementation documentation is not present, it is difficult to determine whether all necessary values are present.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors describe how many simulations were run and the metrics they use. They prsent their results with mean and std deviation. They also describe how many scenarios were run for testing. A full summarised procedure is missing however, so extracting each details for the set up will take a bit of effort.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The method delves deep into the theory of markov models, requiring a deep understanding of it in order to reproduce the work. Solely reyling on the paper is not an option, which is normal for such complex methods. However, the absence of implementation excaserbates this problem as independent investigators have less documentation and examples to rely on.
