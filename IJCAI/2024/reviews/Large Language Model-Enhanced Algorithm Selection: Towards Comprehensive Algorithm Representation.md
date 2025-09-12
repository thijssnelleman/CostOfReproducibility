
## Large Language Model-Enhanced Algorithm Selection: Towards Comprehensive Algorithm Representation
Xingyu Wu, Yan Zhong, Jibin Wu, Bingbing Jiang, Kay Chen Tan
Keywords: Machine Learning: ML: Automated machine learning, Search: S: Algorithm portfolios and configuration, Machine Learning: ML: Applications, Natural Language Processing: NLP: Language models
IJCAI/2024/Proceedings/0579 - Large Language Model-Enhanced Algorithm Selection: Towards Comprehensive Algorithm Representation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide a link to their implementation (https://github.com/wuxingyu-ai/AS-LLM). In the readme they introduce the method and a short description on required libraries. The files are given as a zip, which is a bit of a nuisance. The code has very few comments and some statements contain hardcoded paths which will make execution more difficult. An entry point also seems to be missing. The framework overview in figure 1 does explain the general structure/flow. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(10/10)

The authors use a library for their benchmarks and explain the source. In table 1 they state details on each benchmark of the ten used from the source. As it is a library and the implementation is given, the data should automatically be downloaded through their implementation. Descriptions on each benchmark/task is missing, however due to the amount of them this makes sense. This could have been included in the supplementary materials but can now be found in the cited source on the library.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors state hyperparamter optimisation was done for their method, per benchmark. They do not share what strategy was done, what the exact search space was nor what the outcome values were per experiment. These values can also not be found in the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The evaluation metric used is explained in formula 13. They state the results of table one are achieved by averaging over all instances in each benchmark. The results are single runs per selector. The training procedure of their method is stated in 5.2. They also state how the training and testing set were produced (random selection before the experiment, static onwards). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires and understanding on algorithm selection and NLP.
