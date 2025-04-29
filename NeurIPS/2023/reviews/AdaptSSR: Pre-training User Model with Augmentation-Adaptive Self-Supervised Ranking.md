
## AdaptSSR: Pre-training User Model with Augmentation-Adaptive Self-Supervised Ranking
Yang Yu, Qi Liu, Kai Zhang, Yuren Zhang, Chao Song, Min Hou, Yuqing Yuan, Zhihao Ye, ZAIXI ZHANG, Sanshi Lei Yu
Keywords: 
NeurIPS/2023/Proceedings/71432 - AdaptSSR: Pre-training User Model with Augmentation-Adaptive Self-Supervised Ranking.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/yflyl613/AdaptSSR). In the readme they state installation requirements, a download link to the dataset and how to prepare it and how to run the experiments and where to find more settings/options. The code needs more comments. Structure is doable. Framework overview given in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/2)

The authors provide a download link for the TTL dtaset in the implementation. This dataset is described and statistics given in 4.1 with citation. The authors also use the App dataset. On this a short description and statistics are given but it seems to be a private dataset and the collection strategy is only briefly described. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors discuss HPs at the end of 4.1. One HP is searched over a grid and its selected value is presented in appendix C. Structured overview and acquisition strategy not given (except for 1).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the dataset split in 4.1. as well as the metrics (all standard). The authors repeated experiments 5 times reporting avg + std dev. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on user modeling and self supervised ranking + data augmentation.
