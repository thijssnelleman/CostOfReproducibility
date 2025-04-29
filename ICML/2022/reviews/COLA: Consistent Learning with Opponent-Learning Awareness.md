
## COLA: Consistent Learning with Opponent-Learning Awareness
Timon Willi, Alistair Letcher, Johannes Treutlein, Jakob Foerster
Keywords: 
ICML/2022/Proceedings/16411 - COLA: Consistent Learning with Opponent-Learning Awareness.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. They state in appendix H that it was implemented in PyTorch framework. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/6)

The authors use various games/simulators in their experiments and describe htem in detail with citations in section 5. Parameter values are stated in sec 5 and appendix I.6. Implementation (sources) are not shared.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state various hyperparameters in H.1. and H.2. for different games (experiments). No overview given and no acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors repeated the experiments 10 runs and report the mean variance and consistency of the loss. No data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise in game theory and opponent aware learning.
