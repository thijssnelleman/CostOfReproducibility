
## CaM: Cache Merging for Memory-efficient LLMs Inference
Yuxin Zhang, Yuxuan Du, Gen Luo, Yunshan Zhong, Zhenyu Zhang, Shiwei Liu, Rongrong Ji
Keywords: 
ICML/2024/Proceedings/34310 - CaM: Cache Merging for Memory-efficient LLMs Inference.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/zyxxmu/cam). In the readme they state how to install (seperate readme for that available too), how to run the data generation and how to evaluate, with various examples and parameters. The code needs more comments. The file structure is large and can use some index to explain. The authors provide pseudo code in algorithm 1 and a comparison overview in figure 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(10/10)

The authors use three public LLM testing framework and take six, two and two tasks respectively. On each they provide a citation. They do not provide dtails on the datasets except categorise their tasks. There are no statistics available. The data does seem to autmatically download through the code. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method of the authors (algorithm 1) only has task parameters (Its only parameters defined by the input). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors refer to the metric as 'performance'. The variance in table 1 is not explained. The results are single model. Train/test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries experience with caching, LLMs and NLP tasks.
