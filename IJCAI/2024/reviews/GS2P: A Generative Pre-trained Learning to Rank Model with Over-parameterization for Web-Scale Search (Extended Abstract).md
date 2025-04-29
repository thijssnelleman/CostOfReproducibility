
## GS2P: A Generative Pre-trained Learning to Rank Model with Over-parameterization for Web-Scale Search (Extended Abstract)
Yuchen Li, Haoyi Xiong, Linghe Kong, Jiang Bian, Shuaiqiang Wang, Guihai Chen, Dawei Yin
Keywords: Data Mining: DM: Mining text, web, social media
IJCAI/2024/Proceedings/0936 - GS2P: A Generative Pre-trained Learning to Rank Model with Over-parameterization for Web-Scale Search (Extended Abstract).pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a link to their implementation. They give a framework of their method in figure 1. No details are shared on how the method was implemented, and thus all steps need to be done completely from scratch by following the method explanation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/2)

The authors use two data sets, one which is publicly available and provided a citation on, the other is a private data sets acquired by the authors. On the later they briefly state how large the data set is and how it was annotated, but many details are missing for example regarding the features used in the data set. The publicly available data set is presented with a description but without details, which could be extracted from the citation. However it is difficult to say how comparable the two data sets are to eachother with that much missing information, raising the cost for defending the comparability.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There are no details on hyperparameters although the framework figure definetily suggests they should exist (Method is not parameter free).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors state the metrics used for the experimental setup, for each they provide a citation and a short description. They state they present the average of results, but what is being aggregated is not directly clear, which requires either more expertise on the task or must be reverse engineered by independent investigators.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The method presented requires a good understanding of the task (learning to rank) as well as to follow the steps in their framework much knowledge regarding previous work / SOTA is needed. This is substanially more costly due to the absence of the implementation documentation.
