
## Structure Your Data: Towards Semantic Graph Counterfactuals
Angeliki Dimitriou, Maria Lymperaiou, Giorgos Filandrianos, Konstantinos Thomas, Giorgos Stamou
Keywords: 
ICML/2024/Proceedings/34153 - Structure Your Data: Towards Semantic Graph Counterfactuals.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/aggeliki-dimitriou/SGCE). In the readme the authors introduce the method with an overview, provide installation instructions, how to construct the data labels, how to train the method with various options, some information about their code files, and how to evaluate. There is also a direct link for a data set presented. The code could use a few more comments, as the file structure is overseeable but the code class/method structure is not. Some conditions of the execution of the code and implementation are given in section 4. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

There are five dataset files available in the implementation and a direct link for a sixth. The authors state in 4.1 how they generate ground truth and this code is available in the implementation. For each data set the uauthors provide a citation, description and key statitstics. The authors provide the latter data set available in the implementation, however the first one is obscure. The other datasets are regarding additional experiments from the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

In appendix C the authors summarise the hyperparameter values per experiment but a full overview is missing. This is clarified in the implementation docs. The authors state 'Best results were achieved' in the appendix, but don't state what strategy or budget was used to achieve this. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in section 4 and describe them briefly. The results are single runs. There are some mentions of test sets in the paper, but it is never clarified how these are derived. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in geometric deep learning, CV and counterfactuals. 
