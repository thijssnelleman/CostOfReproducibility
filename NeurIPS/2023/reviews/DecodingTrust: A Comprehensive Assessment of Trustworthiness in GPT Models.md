
## DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie, Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi Xiong, Ritik Dutta, Rylan Schaeffer, Sang Truong, Simran Arora, Mantas Mazeika, Dan Hendrycks, Zinan Lin, Yu Cheng, Sanmi Koyejo, Dawn Song, Bo Li
Keywords: 
Award: Outstanding Datasets and Benchmarks Paper
NeurIPS/2023/Proceedings/2449 - DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models.pdf
Project URL: https://decodingtrust.github.io

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors link their implementation on the project page (https://github.com/AI-secure/DecodingTrust). In the readme they index it, show the project structure in great detail, how to install, and various tutorials and tips. The code is in general well documented with comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(18/18)

The authors list the datasets used per task/experiment in appendix A. The datasets are described with citations and statistics in appendix E. Direct links in the implementation. The authors also create several datasets themselves regarding prompts which are present in the implementation which we count as one dataset.  Dataset statistics also available in appendix K.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

N/A

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use many metric types which are defined in appendix C to J. The authors evaluate various single LLMs over the datasets (no training done I think).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires knowledge on all fronts of LLM evaluation techniques.
