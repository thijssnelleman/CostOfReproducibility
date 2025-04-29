
## MMVQA:  A Comprehensive Dataset for Investigating Multipage Multimodal Information Retrieval in PDF-based Visual Question Answering
Yihao Ding, Kaixuan Ren, Jiabin Huang, Siwen Luo, Soyeon Caren Han
Keywords: Natural Language Processing: NLP: Applications, Natural Language Processing: NLP: Resources and evaluation, Natural Language Processing: NLP: Information extraction
IJCAI/2024/Proceedings/0690 - MMVQA:  A Comprehensive Dataset for Investigating Multipage Multimodal Information Retrieval in PDF-based Visual Question Answering.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state they provide the implementation documentation link + appendix (https://github.com/adlnlp/mmvqa). However the repository only contains a readme. Here they provide links to the data set downloads. The authors do provide links for libraries used to collect the data. However the evaluation of the baselines' code and their framework is not given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors present a new data set, which they publish in their implementation documentation. They provide extensive details on it regarding the features/structure of the data and do an analysis on it in section 4, describe the tasks in section 5 and suggest metrics for the task.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors use pretrained models. They state in section 6.2 for the model / configuration details the appendix should be used. However this is not present in the paper and cannot be found in the implementation documentation (although it is stated it should be there). In general the lack of this information makes the effort extremely high, but if it were presented this could be a 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used for each task, and analyse the effect of various input sizes. The exerpiments indicate single run results, and as the models are pretrained, no training procedure is stated. A summary on the experimental procedure would be welcome, but this should be extractable with some effort.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a thorough understanding of NLP / Text data mining. The absence of the appendix / implementation means the independent investigator will have to rely more on external sources to grasp and reproduce the presented method. The full and clear documentation on the presented data set lowers this.
