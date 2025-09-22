## Chain-of-Experts: When LLMs Meet Complex Operations Research Problems
Ziyang Xiao, Dongxiang Zhang, Yangjun Wu, Lilin Xu, Yuan Wang, Xiongwei Han, Xiaojin Fu, Tao Zhong, Jia Zeng, Mingli Song, Gang Chen
Keywords: 
ICLR/2024/Proceedings/18977 - Chain-of-Experts: When LLMs Meet Complex Operations Research Problems.pdf
Project URL: https://openreview.net/attachment?id=HobyL1B9CZ&name=supplementary_material

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Explanation:
Implementation available (https://github.com/xzymustbexzy/Chain-of-Experts) , start with 1.

Installation requirements: there is a txt file. Repository structure is self-explaining. Data links(!)/processing: data is uploaded in repo, new dataset is in review stage. README has clear information how to run the code, no increasment. +0

Looked at main.py, run_exp.py. Functions functionalities are often described in definition, but less than 50% of the code is commented. +1

Repo is easy to navigate. +0


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1 increment for neiter dataset, so average score of 2)

(2/2)

1. Dataset: LPWP
The LPWP dataset is uploaded in the repo, which is for me a direct link. +0
Dataset described in section 4.1. +0
Concerning statistics, there is only the info that there are 713 training, 99 val and 289 test problems, which is limited. +1 (e.g. there could be stats that classify the kind of OR problem aoart from "elementary-level".)
Not partially private since uploaded in repo. +0

2. Dataset: ComplexOR
Authors say dataset will be uploaded. However, it seems that parts are already the files uplaoded (raw version), so it seems accessible. +0
Dataset described in section 4.1. +0
Concerning statistics, there is only the info that there are 37 problems, which is limited. +1
Not partially private since uploaded in repo. +0

As far as I understand, there are no synthetic data generators.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The paper uses ChatGPT, so they are relatively few hyperparameters. They state the used temperature and experimental setup in section 4.2
Thus, I would not expect any table or overview. +0

I feel like all hyperparameters are disclosed. +0

The authors perform an parameter sensitivity analysis.
Thus, they have a strategy. +0
However, the budget is not clear. + 1


### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The used metrics (accuracy, CE/RE rate) are explained in 4.2. +0

For LPWP train/val/test is specified, for ComplexOR I think they use all 37 problems. +0

Strategy is detailed in 4.2 +0

The aggregation just seems to be the named metrics, thus +0.


### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Readers need basic knowledge of OR and LLMs. However, the paper is basically just prompting, so I think it does not need so much expertise.