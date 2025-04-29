
## Completeness and Diversity in Depth-First Proof-Number Search with Applications to Retrosynthesis
Christopher Franz, Georg Mogk, Thomas Mrziglod, Kevin Schewior
Keywords: Search: Search and Machine Learning, Agent-based and Multi-agent Systems: Algorithmic Game Theory, Multidisciplinary Topics and Applications: Life Science, Planning and Scheduling: Planning Algorithms
Award: Distinguished Paper
IJCAI/2022/Proceedings/0658 - Completeness and Diversity in Depth-First Proof-Number Search with Applications to Retrosynthesis.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. They use previously known algorithms and provide a proof on them, with an adaptation to 'multiple solutions'. This implementation is not given only described. No pseudo code or visualisations are given, practical details are missing. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1/1)

The authors use a data set constructed from two others, a public data set which they cite, and another provided by 'Bayer chemists' (No other information given). This data set is publicly available and linked. More descriptions and statistics would be needed to give a full picture on this data regarding comaparability and acquisition. The authors also train an ANN on '31 million reactions' and state these were 60% publicly gather and 40% private. Details on this data set are few and is seemingly private. They state this part of the setup and not of the actual experiment.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors set the maximum runtime of each algorithm. Other than that their algorithm used in the experiment is parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used in 6.2. They ran it on the dataset published online. The experiment was run under various computation time budgets. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requries an understanding of the problem (chemistry/biology), the two methods used (DFPN and MCTS) and previous theoretical work regarding 'completeness' of DFPN.
