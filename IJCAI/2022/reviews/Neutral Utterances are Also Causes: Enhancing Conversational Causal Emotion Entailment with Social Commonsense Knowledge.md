
## Neutral Utterances are Also Causes: Enhancing Conversational Causal Emotion Entailment with Social Commonsense Knowledge
Jiangnan Li, Fandong Meng, Zheng Lin, Rui Liu, Peng Fu, Yanan Cao, Weiping Wang, Jie Zhou
Keywords: Natural Language Processing: Sentiment Analysis and Text Mining, Natural Language Processing: Text Classification
IJCAI/2022/Proceedings/0584 - Neutral Utterances are Also Causes: Enhancing Conversational Causal Emotion Entailment with Social Commonsense Knowledge.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/LeqsNaN/KEC). In the readme they state the requirements, link the repositories their implementation is based on, link a dataset ("additional data"), and a short summary on a few code files where they link another dataset and state where it should be placed. The code has very few comments. They also link their appendix in the readme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors state the dataset used in 4.1 wtih citation and link from where it was collected. Details regarding pre-processing are stated and in table 1 the provide staistics on the data. The data is linked in the repository. A full description, but more details are found in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in 4.3. The full hyperparameter space can be found in the main entry point of the implementation. Various values are stated and for each a default value can be found which can fill the gap if any are missing (Would have to be assumed). There is no acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in 4.3 (standard). They state the experiments are conducted under 5 different seeds. There seems to be some variance indicated in table 2. The aggregation and variance are not specified. The train/dev/test split is specified in table 1 (static).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on NLP and sentiment analysis.
