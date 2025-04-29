## DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, Sang Truong, Simran Arora, Mantas Mazeika, Dan Hendrycks, Zinan Lin, Yu Cheng, Sanmi Koyejo, Dawn Song, Bo Li
Keywords: 
Award: Outstanding Datasets and Benchmarks Paper
NeurIPS/2023/Proceedings/2449 - DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models.pdf
Project URL: https://decodingtrust.github.io

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Starting with 1 since there is code available. No extra cost since there are clear instructions for setup and running the code. There are comments and function descriptions in the main part of the code but also many files with almost no comments, +1. Repository structure is easy to navigate, no extra cost.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

There is a direct link to a website with detailed description and a detailed github repo. The dataset is public. In appendix E they provide basic statistics.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors center their evaluation around black-box LLMs such as GPT-4 and GPT-3.5, for which they do not have access to hyperparemeters. Also, it appears to me that for the benchmark generation, parameters are not that important in this case. No hyperparameter space, values or acquisition is defined (probably because thats not applicable). So because it seems not relevant, I stick to the rating of 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metric, toxicity, is explained, the data is explained in depth, the strategy is explained and the results are clearly aggregated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

I think one can understand and reproduce the paper fearly easy, since it depends on using tools. The paper is rather non-technical and focuses on non-toxic content generation rather than something more complicated such as code generation. Still, I give a 3 since it might be difficult to exactly reproduce the benchmark.