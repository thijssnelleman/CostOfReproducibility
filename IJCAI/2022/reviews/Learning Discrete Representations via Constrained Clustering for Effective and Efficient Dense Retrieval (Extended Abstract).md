
## Learning Discrete Representations via Constrained Clustering for Effective and Efficient Dense Retrieval (Extended Abstract)
Jingtao Zhan, Jiaxin Mao, Yiqun Liu, Jiafeng Guo, Min Zhang, Shaoping Ma
Keywords: Artificial Intelligence: General
IJCAI/2022/Proceedings/0754 - Learning Discrete Representations via Constrained Clustering for Effective and Efficient Dense Retrieval (Extended Abstract).pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/jingtaozhan/RepCONC). Here they have an index in the readme, expalnation of the method, installation instructions, how to use explanation with full tutorials including scripts to execute directly regarding data set preperation directory structure explanations. The code has some comments but could definetily use some more.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors have automatic data downloaders in their implementation examples. They state they use two benchmark datasets (with citations) but only present results on one due to space limitations and refer to their full paper elsewhere with link. Data downloader is available in the examples of the implementation. The authors state a some statistics on this data set in their paper, no description on the data is found. This is also not present in their full paper which they link in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify their hyper parameter values in the full version of the paper. They are fully specified and easily checkable against their formulas and implementations. They do not state an acquisition method for these parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors do not specify exactly how the experiments are conducted with a dedicated section. The results indicate single runs. The authors specify the data sets have static tests sets, the metrics are breifly stated in 4.1 of the full paper but not explained or cited ("official metrics"). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on  information retrievel and compression.
