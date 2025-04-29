
## Recall, Retrieve and Reason: Towards Better In-Context Relation Extraction
Guozheng Li, Peng Wang, Wenjun Ke, Yikai Guo, Ke Ji, Ziyu Shang, Jiajun Liu, Zijie Xu
Keywords: Natural Language Processing: NLP: Information extraction
IJCAI/2024/Proceedings/0704 - Recall, Retrieve and Reason: Towards Better In-Context Relation Extraction.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state a github link which does not work, and unclear whether this would have been their implementation. No other implementation details are given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors state the publicly ('commonly used') data sets used in 3.1 and provide citations + statistics on them in table 1. They provide a direct link in the footnotes. No descriptions are given on the datasets or their tasks. They use opensource pretrained models and provide citations on them.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state a few hyperparameters in the experiment details. It is not stated how these were acquired nor is it clear if all needed values are given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the training procedure in the experiment details. The data set splits are static and details in table 1. They present their test set results and state they use micro-f1 in table 2 caption, but do not explain what this metric is. The results and descriptions indicate single run/model results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires an understanding of RE. The absence of implementation means the whole procedure needs to be reimplemented thus requiring more experience on used domains such as LLMs.
