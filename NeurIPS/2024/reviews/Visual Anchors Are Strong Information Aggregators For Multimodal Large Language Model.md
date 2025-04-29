
## Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model
Haogeng Liu, Quanzeng You, Xiaotian Han, Yongfei Liu, Huaibo Huang, Ran He, Hongxia Yang
Keywords: 
NeurIPS/2024/Proceedings/96811 - Visual Anchors Are Strong Information Aggregators For Multimodal Large Language Model.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/liuhaogeng/Anchor-Former). In the readme they describe the code in 'parts' (cryptic) and reference another repository. The code can use more comments. No installation instructions. Overview given in figure 3, pseudo code in figure 7.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(9/9)

The authors list the data sets used with citations, brief descriptions and metrics used in Table 7 of the appendix F. No direct links or statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors summarise the hyperparmaeters used in section 4.1 under the implementation details. However it is a very informal summary and no acquisition is specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics per data set are given in table 7, two are not standard other 3 are (only standard for NLP subfield). Are results are single model and the training set is specified in 4.1 (all data sets are test sets in the results). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in NLP, LLM and vision-language connectors.
