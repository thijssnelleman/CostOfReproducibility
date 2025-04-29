
## Visual Similarity Attention
Meng Zheng, Srikrishna Karanam, Terrence Chen, Richard J. Radke, Ziyan Wu
Keywords: Computer Vision: Interpretability and Transparency, Computer Vision: Image and Video retrieval, Computer Vision: Representation Learning, Computer Vision: Segmentation, Computer Vision: Transfer, low-shot, semi- and un- supervised learning
IJCAI/2022/Proceedings/0241 - Visual Similarity Attention.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors sate in section 4 briefly in which framework/library (and language implied) they developped their implementation. A general overview of the solution is shown in figure 1 and 2 but no detailed overview of the entire method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/3)

The authors state the used datasets in 4.1, with citations. No descriptions, statistics or other details on the data/tasks are presented. They all do seem to be public, but this is not explicitly stated.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors introduce a parameter (loss weight) in section 3.3. In section 4.2 the authors state the value of this parameter, and a few other training parameter values. An overview of the HP space is missing. No acquisition strategy specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors state they use a protocol from a previous work in 4.1 with citation. They state the metric used for evaluation with a citation but no description/explanation. There are no details specified on how training/testing was divided in the paper. Results seem to be single model/run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on attention mechanisms and computer vision, practical experience with it as well as the implementation details are missing and a lot of the details regarding data set usage as well meaning this will have to be reverse engineered.
