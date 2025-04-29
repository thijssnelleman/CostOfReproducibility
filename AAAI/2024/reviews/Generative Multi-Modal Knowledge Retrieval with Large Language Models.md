
## Generative Multi-Modal Knowledge Retrieval with Large Language Models
Xinwei Long, Jiali Zeng, Fandong Meng, Zhiyuan Ma, Kaiyan Zhang, Bowen Zhou, Jie Zhou
Keywords: NLP: Information Extraction, NLP: (Large) Language Models, NLP: Language Grounding & Multi-modal NLP
AAAI/2024/Proceedings/31456 - Generative Multi-Modal Knowledge Retrieval with Large Language Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

Implementation details are provided in the paper. The authors provide a Github repository in their paper (https://github.com/xinwei666/MMGenerativeIRThe), and also link another repository used for database storage and look ups. The authors provide installation notes in their read me, details on the repository structure, links to the data used and data processing steps. Explanations on how to train and evaluate the method are also presented. The code has an argument parser with help string, but other than that seems a bit poor in terms of comments to understand what exactly is going on (Also no type hinting etc.). If this was present, the cost would be maximally minimised by the authors.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three publicly available benchmark data sets and cite their source, provide their data processor in the implementation and link the source where to download. They provide meta information on the data sets in the paper. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors denote key hyper parameter values in their paper, and more default values can be found in their repository. It is unclear how these values were achieved.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the evaluation metrics used with their motivation. There are many details available, but the exact procedure is not named, could be single runs. However with the presence of the implementation documentation this could be easily derived.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The method requires a degree of understanding of LLMs, but the method is well documented including examples and functional code, thus lightening the entry level of expertise required to reproduce it.
