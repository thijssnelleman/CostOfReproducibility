
## Case-Based Reasoning with Language Models for Classification of Logical Fallacies
Zhivar Sourati, Filip Ilievski, Hông-Ân Sandlin, Alain Mermoud
Keywords: Natural Language Processing: NLP: Information retrieval and text mining, AI Ethics, Trust, Fairness: ETF: Explainability and interpretability, Knowledge Representation and Reasoning: KRR: Case-based reasoning
IJCAI/2023/Proceedings/0576 - Case-Based Reasoning with Language Models for Classification of Logical Fallacies.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/zhpinkman/CBR). In the readme they introduce the method, provide installation requirements, an index on the explanations following in the readme, a direct download link to the cache, a citation link to the original work for the data and where the data can be found where it has its own readme, explanations of scripts in each directory and how to adapt the configuration for your own setting. The code is well documented, although its a bit shy on in code comments. The configurations are hardcoded into the code. Their pipeline is summarised in figure 1. They state implementation details at the end of section 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors state the data sets used with citations and describe them. They provide a few statistics on them. The data is available in the implementation documentation. A bit more statistical data on the datasets would be welcome, but can be extracted from the implementation or the citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state in section 4 the parameters used for a model they use from a previous work and analyse the the performance over various parameters on their method. More hyperparameter values can be found in the implementation. No details on acquisition of these are stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used for the experiments in section 4, which are standard. The authors also state the train split for one, and note the other is only evaluated on for generalisation testing. The results indicate single run/model experiments.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in NLP to follow the task and previous work used (SOTA).
