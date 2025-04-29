
## Long-term Spatio-Temporal Forecasting via Dynamic Multiple-Graph Attention
Wei Shao, Zhiling Jin, Shuo Wang, Yufan Kang, Xiao Xiao, Hamid Menouar, Zhaofeng Zhang, Junshan Zhang, Flora Salim
Keywords: Data Mining: Mining Spatial and/or Temporal Data, Multidisciplinary Topics and Applications: Smart Cities
IJCAI/2022/Proceedings/0309 - Long-term Spatio-Temporal Forecasting via Dynamic Multiple-Graph Attention.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide a large overview on their method in figure 2, pseudo code can be found in algorithm 1, and the details on some attention mechanism in figure 3. The implementation is not published. No practical details given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors state the datasets used in 3.1 with descriptions, citations and some statistics in 3.1. On the first one a direct link is provided. They are both seemingly public ("published"). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state the hyperparameters in section 3.2. Although algorithm 1 states input parameters, these do not overlap with the parameter values stated so the space is unclear. No acquisition strategy specified. The parameters are stated per dataset.  

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in 3.2 (standard). There is no specification how the data was split for training/testing, only statemetns such as "all the tests were trained for 40 epochs" and "All the tests used a 24-time step historical time window". The results presented are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires experience with spatio temporal data, geometrical deep learning and attention mechanisms.
