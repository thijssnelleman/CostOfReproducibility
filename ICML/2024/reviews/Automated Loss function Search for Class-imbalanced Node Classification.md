
## Automated Loss function Search for Class-imbalanced Node Classification
Xinyu Guo, KAI WU, Xiaoyu Zhang, Jing Liu
Keywords: 
ICML/2024/Proceedings/34182 - Automated Loss function Search for Class-imbalanced Node Classification.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. A schematic diagram on the method is available in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(5/5)

The authors state the data sets used in 5.1, provide citations on them but statistics and general descriptions are missing. No direct links provided. The extra details in appendix A provide little information on the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

In 4.1 the authors state the input of their method (dataset, model and metric). This makes the method seemingly parameter free. It is confusing however as they state they use MCTS in their algorithm which is parameterised with a budget. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors refer for the data set splits in the appendix A to a previous work. The metrics used in the results are standard. The experiments are repeated either ten or three times. The authors present the results as mean with standard error. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on loss function search, a bit of GNNs and imbalanced classification. 
