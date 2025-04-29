
## PINA: Leveraging Side Information in eXtreme Multi-label Classification via Predicted Instance Neighborhood Aggregation
Eli Chien, Jiong Zhang, Cho-Jui Hsieh, Jyun-Yu Jiang, Wei-Cheng Chang, Olgica Milenkovic, Hsiang-Fu Yu
Keywords: 
ICML/2023/Proceedings/24591 - PINA: Leveraging Side Information in eXtreme Multi-label Classification via Predicted Instance Neighborhood Aggregation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/amzn/pecos/tree/mainline/examples/pina). In the readme they state installation instructions and how to run the code. They also reference another repository. The code could use some more comments. In figure 3 and 4 they give a detailed overview on the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The implementation has a dataset downloading script. The authors provide a citation and explanation on them in section 5.1 and staitstics in table 1. Three out of four data sets can be downloaded from the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors specify parameter details in appendix F on their acquisition (for the models they lend them from previous works) and their full specifiations are available in the implementation as configuration files.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they report two metrics which are standard in NLP. Formulas are provided in appendix F. The data sets have static splits in training/testing. Results are single method.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in NLP/Transformers and extreme multi label classification. 
