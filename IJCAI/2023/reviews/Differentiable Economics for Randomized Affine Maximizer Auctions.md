
## Differentiable Economics for Randomized Affine Maximizer Auctions
Michael Curry, Tuomas Sandholm, John Dickerson
Keywords: Game Theory and Economic Paradigms: GTEP: Mechanism design, Game Theory and Economic Paradigms: GTEP: Auctions and market-based systems, Multidisciplinary Topics and Applications: MDA: Economics
IJCAI/2023/Proceedings/0293 - Differentiable Economics for Randomized Affine Maximizer Auctions.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. They do refer for 'diagrams and pseudo code' to the supplementary material which is not present nor linked. One mention of a library is done in section 5 (JAX).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/1)

The authors consider the problem of a combinatorial auction setting (4.1), and consider various settings. As there are no details on how this was simulated, this ties into the problem of the lack of implementation. The auction is explained in detail.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors state their hyperparameter values in 6.1. It is difficult to evaluate if all needed HP values are given. There are no details on how the presented values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the training procedure in 6.1 and how many samplings were done for testing. In the results table these are aggregated (mean?). The metric is a simulation based metric (revenue from the auction).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires a lot of previous experience with differentiable economics and the task (auction bidding) as many details are left obscured in the work thus must either be found in the citations or other previous work. The absence of the implementation and unclarity on what simulator is used worsens this. 
