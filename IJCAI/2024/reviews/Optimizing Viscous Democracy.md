
## Optimizing Viscous Democracy
Ben Armstrong, Shiri Alouf-Heffetz, Nimrod Talmon
Keywords: Game Theory and Economic Paradigms: GTEP: Computational social choice, Agent-based and Multi-agent Systems: MAS: Agent-based simulation and emergence, Multidisciplinary Topics and Applications: MTA: Web and social networks
IJCAI/2024/Proceedings/0292 - Optimizing Viscous Democracy.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors present a theoretical analysis of viscous democracy over liquid democracy. In section seven they present an experimental analysis on this, and state they use SciPy for a part of their implementation. However, their own implementation source is missing, and no details on it are given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/2)

The authors use social networks that they collected from 'a variety of sources' for which they cite a source. They also generate artifical networks, for which they also cite a source. As the implementation is missing, these sources will have to be investigated and thoroughly analysed in order to understand how this was actually done in this work.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors use monte carlo simulations to calculate group accuracy, for which they state 1000 simulations (elections) are done. For this number they cite a source. No other parameters present.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the number of trials and size of the population per trials in 7.2 and 7.3. The procedure is relatively straight forward, although the parameters may be complex to understand and apply.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires a experience in the simulations conducted, as the problem statement has some complex graph mathematics. This could have been made more accesible with implementation documentation as it could serve as an example to the problem.
