
## Scalable Multiple Kernel Clustering: Learning Clustering Structure from Expectation
Weixuan Liang, En Zhu, Shengju Yu, Huiying Xu, Xinzhong Zhu, Xinwang Liu
Keywords: 
ICML/2024/Proceedings/33226 - Scalable Multiple Kernel Clustering: Learning Clustering Structure from Expectation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The paper is mainly a theoretical one but in section 6 the authors do validate their theory through experiments. However a link to their impleemntation is not shared. In algorithm 1 pseudo code is given on their mehod. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(11/11)

The author summarise the datasets used in batle 1 with some statistics. They are briefly summarised in 6.1, and direct links provided in appendix B. There are no citations presented on the datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors introduce their algorithm parameters in algorithm 1. None of these seem to be configurable e.g. are part of the input/problem definition. This is also re-iterated in 6.2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use 4 metrics for the evaluation. The acronyms are explained in 6.2. However the emaning of each is problem/task specific and the reader is expected to understand these. The results are single runs. No training/testing split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on clustering and unsupervised learning, as well as the theory behind it. The lack of implementation means the presented documentation will have to be used to re-produce it in order to reprdouce the work.
