
## On the Representation Collapse of Sparse Mixture of Experts
Zewen Chi, Li Dong, Shaohan Huang, Damai Dai, Shuming Ma, Barun Patra, Saksham Singhal, Payal Bajaj, XIA SONG, Xian-Ling Mao, Heyan Huang, Furu Wei
Keywords: 
NeurIPS/2022/Proceedings/53300 - On the Representation Collapse of Sparse Mixture of Experts.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a link in the subtitle of the paper but this link does not work (can't connect). Overview of the method given in figure 1. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(8/9)

The authors state 2 datasets in 4.1 for pretraining data, CCNet with citation but Wikipedia dump is only named. The authors use benchmarks from XTREME namely Universal Dependencies, WikiAnn, XNLI, PAWS-X, MLQA, XQuAD and TyDiQA-GoldP (all citations provided). No details provided on the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters are detailed in appendix A-C with full tables. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors present their results averaged over 5 runs (random seed). Metrics are F1 score, EM and Perplexity but latter two are not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP.
