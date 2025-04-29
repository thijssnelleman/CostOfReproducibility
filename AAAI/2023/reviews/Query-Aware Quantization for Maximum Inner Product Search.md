
## Query-Aware Quantization for Maximum Inner Product Search
Jin Zhang, Defu Lian, Haodi Zhang, Baoyun Wang, Enhong Chen
Keywords: DMKM: Web Search & Information Retrieval, DMKM: Web Personalization & User Modeling
AAAI/2023/Proceedings/25613 - Query-Aware Quantization for Maximum Inner Product Search.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide no implementation source but state it was implemented in Julia and run on Linux with some details. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three benchmark data sets and provide citations on them. The authors provide details and statistics on them and state more can be found in the appendix (which is not present due to AAAI limitations). In general well documented, however the implementation source would help in case any processing is done before using.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors provide a few details on the hyperparameters, but not on how their values were found. The authors refer to the appendix for detailed settings on the hyperparameters. This is missing due to AAAI limitations. If the authors had provided any link to this appendix this could have been 1-3 value.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors clearly explain their evaluation metrics. They present single run results in their graphs. There are no details provided on training/testing splits however on the datasets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method requires some understanding of the task (recommender systems) and the matrix math behind the method. 
