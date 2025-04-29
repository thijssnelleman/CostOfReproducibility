
## Decentralized Gossip-Based Stochastic Bilevel Optimization over Communication Networks
Shuoguang Yang, Xuezhou Zhang, Mengdi Wang
Keywords: 
NeurIPS/2022/Proceedings/54181 - Decentralized Gossip-Based Stochastic Bilevel Optimization over Communication Networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors specify in the checklist the code will be provided via github link in the camera ready phase. This is not found.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors state they use Australia handwriting dataset in section 6 with citation. They also consider the bellman minimzation problem (synthetic) and specify details in appendix E.2. as well but not the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state let their method conduct HPO in sec 6. Their own method in algorithm 2 takes in four parameters. Iteration T given per experiment. K is regarding the optimisable model. The parameter values are stated in section 6. Acquisition not applicable as it is an HPO task.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Results are presented over training/validation loss in figure 2 averaged over total samples with various valous of parameter K, each generated through 10 independent simulations. In figure 3 they state averaged MSE for the same settings. The data split is randomly done in sec 6 but proportions are not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on bilevel optimization.
