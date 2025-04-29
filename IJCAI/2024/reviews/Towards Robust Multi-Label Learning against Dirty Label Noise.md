
## Towards Robust Multi-Label Learning against Dirty Label Noise
Yuhai Zhao, Yejiang Wang, Zhengkui Wang, Wen Shan, Miaomiao Huang, Meixia Wang, Min Huang, Xingwei Wang
Keywords: Machine Learning: ML: Multi-label learning, Machine Learning: ML: Optimization, Machine Learning: ML: Weakly supervised learning
IJCAI/2024/Proceedings/0617 - Towards Robust Multi-Label Learning against Dirty Label Noise.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a source on their implementation. Pseudo code is given in algorithm 1. No details regarding the implementation are specified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(14/14)

The authors use ten data sets in section 4.1 for which they provide a source, and statistics on the data in table 2. They also state they generate three synthetic data sets with details on the generation, but no implementation of the generator is given. A direct link is missing. The absence of the description of the data is logical due to the number, but an appendix on it would have been welcome. In 4.3 they state another large data set which they cite and provide details on. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state three parameters for their algorithm in section 3.2, but these are not presented in algorithm 1. An ablation analysis is conducted, but what the values were in the experiments is not clarified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state they use four metrics to evaluate but do not explain them (although one is clearly standard, the others are possibly subfield standard but this is not noted so requires expertise). They present their results with an aggregation plus some variance but where these values come from is not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries decent previous expertise and knowledge of SOTA in MLL. Also requires understanding of the problem to grasp the theoretical proofs presented.
