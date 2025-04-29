
## Community detection in sparse latent space models
Fengnan Gao, Zongming Ma, Hongsong Yuan
Keywords: 
JMLR/2022/Proceedings/201036 - Community detection in sparse latent space models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state pseudo code in algorithm 1, 2 and 3. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors conduct simulation studies in section 4 and specify the simulator with parameter and values but no implementation. In section 5 the authors use 5 real datasets, provide high level statistics descriptions and citations but some details could be better. No direct links. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Algorithm 1-3 all require a number of clusters c (semantical) and latent dimension d for 1 and 3 and algorithm 2 requires number of iterations R. The iterations R is varied for the experiment between 1 and 10. The other parameters seem not to be used for the experiment (section 4 states 'This reassures that repeated initializations in Algorithm 3 were only needed for technical reasons in proofs, and justifies the use of SpecLoRe in practice').

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate error rate (percentage) of misclassification and runtime in seconds. For the simulated results they are averaged over 100 repetitions. no data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on spectral clustering.
