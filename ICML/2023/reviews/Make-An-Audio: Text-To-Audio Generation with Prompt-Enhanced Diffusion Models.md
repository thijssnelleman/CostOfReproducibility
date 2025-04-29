
## Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models
Rongjie Huang, Jiawei Huang, Dongchao Yang, Yi Ren, Luping Liu, Mingze Li, Zhenhui Ye, Jinglin Liu, Xiang Yin, Zhou Zhao
Keywords: 
ICML/2023/Proceedings/25060 - Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models.pdf
Project URL: https://make-an-audio.github.io

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors share a link to their project wit h some examples but not their implementation. Figure 2 and 3 have an overview of the method. In 4.2 the authors state a framework used for parts of their implementation. There are notes on the implementation in appendix E. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(15/15)

The authors use 15 data sets as stated in 5.1. In appendix A table 4 these are summarised with citations / direct links. Descriptions and statistics are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

In table 6 of appendix B the authors summarise hyperparameter values of their models. They are mainly architecture variables. The summary is incomplete. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors detail their evaluation in appendix C, where they state how the human ratings were acquired and explain the metric. In 5.3. the authors introduce four other metrics with citations and brief descriptions. The authors use a two data sets for evaluation (test set), one as zero-shot scenario. The variance is over human evaluation population with mean and 95% confidence interval. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries experience with audio task and generation. 
