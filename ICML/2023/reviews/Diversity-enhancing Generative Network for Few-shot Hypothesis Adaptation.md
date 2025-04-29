
## Diversity-enhancing Generative Network for Few-shot Hypothesis Adaptation
Ruijiang Dong, Feng Liu, Haoang Chi, Tongliang Liu, Mingming Gong, Gang Niu, Masashi Sugiyama, Bo Han
Keywords: 
ICML/2023/Proceedings/25010 - Diversity-enhancing Generative Network for Few-shot Hypothesis Adaptation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors do not provide their implementation. In appendix C they state they developed it in PyTorch. 1.7.1 and which python version. An overview on the method is given in figure 2 and pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors use three digits and three objects benchmarks datasets. There is a description on the task given and a short one with citations in appendix B on the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify the hyperparmaeter settings in appendix C. The acquisition for some is not applicable but for a few it is an is not specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors report accuracy + std dev as metrics. There is no specification on training vs testing. There is no clear specifcation on what is being aggregated in the tables.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on few shot learning.
