
## One Model for All Domains: Collaborative Domain-Prefix Tuning for Cross-Domain NER
Xiang Chen, Lei Li, Shuofei Qiao, Ningyu Zhang, Chuanqi Tan, Yong Jiang, Fei Huang, Huajun Chen
Keywords: Natural Language Processing: NLP: Information extraction, Natural Language Processing: NLP: Named entities
IJCAI/2023/Proceedings/0559 - One Model for All Domains: Collaborative Domain-Prefix Tuning for Cross-Domain NER.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/zjunlp/DeepKE/tree/main/example/ner/cross). Here they state installation requirements, how to fetch the data used and an explanation of its format, how to train the method and an acknowledgement regarding which repository they based their implementation on. The code has a decent amount of comments and most of it seems to be written in a single file, which reduces the complexity of the directory structure but may complicate understanding this file.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors state in 4.1 they use four publicly available data sets, include citations on each and provide a short description on one of them. No statistics are provided. All datasets are directly available in the implementation documentation. However the implementation documentation seems to imply also a training procedure on which nothing is specified in the paper. This will require a deeper investigation to verify.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The method does not discuss parameters/values but the implementation documentation does indicate a lot of parameters. However it is very unclear what is relevant to the presented results and what is not.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics in the caption of table 1 (F1-score, standard) and explain how the 'average' is calculated briefly. The results indicate single model/run performance. The implementation docs also imply training procedure which is not documented in the paper regarding the experiments.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience in NLP to understand the task and method, as the presented problem it is not straightforward.
