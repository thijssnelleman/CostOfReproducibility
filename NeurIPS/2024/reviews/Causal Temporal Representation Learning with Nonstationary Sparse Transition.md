
## Causal Temporal Representation Learning with Nonstationary Sparse Transition
Xiangchen Song, Zijian Li, Guangyi Chen, Yujia Zheng, Yewen Fan, Xinshuai Dong, Kun Zhang
Keywords: 
NeurIPS/2024/Proceedings/95735 - Causal Temporal Representation Learning with Nonstationary Sparse Transition.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation in S3.3. (https://github.com/xiangchensong/ctrlns). In the readme they state installation instructions, how to generate the data, how to run training for various experiments, a result of the paper and a real-world experiment link. The code has few comments. The structure is large without an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use a synthetic dataset for which they provide code. The synthetic generation is described in S2.1. with statistics of what they generated and these overlap with the parameters of the generator code. The real world datasets are described in S2.2 briefly with citation. More information on the real world datasets would be welcome. The datasets have links in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

HP details are given in S3.4. in an informal summary in the text where they are stated for the synthetic experiments. The model design for the real world data is discussed in 5.2. and in S3.4. they state they 'follow the values' of a baseline method. A full overview of the parameters is missing. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors repeated the experiment with three random seeds and present average + std dev for synthetic and 'default' 10 fold dataset split for hollywood and 5 random seeds again for crosstask but no data split description. The evaluation metrics are described in 5.1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on causal temproal learning.
