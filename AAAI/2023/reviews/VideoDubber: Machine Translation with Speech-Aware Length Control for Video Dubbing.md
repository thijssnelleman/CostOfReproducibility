
## VideoDubber: Machine Translation with Speech-Aware Length Control for Video Dubbing
Yihan Wu, Junliang Guo, Xu Tan, Chen Zhang, Bohan Li, Ruihua Song, Lei He, Sheng Zhao, Arul Menezes, Jiang Bian
Keywords: SNLP: Machine Translation & Multilinguality, SNLP: Speech and Multimodality
AAAI/2023/Proceedings/26613 - VideoDubber: Machine Translation with Speech-Aware Length Control for Video Dubbing.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

There is no implementation source provided in the paper. There is a section dedicated to the model architecture, with a figure describing it with some details, but no real details on the implementation are given, making it a gigantic effort to re-implement.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(0/1)

The authors state they construct a data set of their own to make up for the lack of real-world data sets, which the authors motivate by discussing the issues with available benchmark data sets(not realistic). The authors provide an url for building the test set (https://speechresearch.github.io/videodubbing/) and a url for demo-samples of their experiment output (https://speechresearch.github.io/videodubbing/). The data set is seemingly not publicly available. The authors state they use other data sets for training which they cite, and state that they are public. They state the private acquired data set is used for evaluation, and part of the public is also used for evaluation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The author provide details on the models architecture, such as width and activation functions. however, no other details are given such as learning rate or batch sizes, nor how this architecture was acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide a detailed description on their evaluation and objective metrics. They also discuss some subjective metrics. They present single model results in their tables. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The method requires a good understanding of transformers and machine translation. The lacking details regarding implementation and algorithm configuration have a serious impact on the amount of expertise acquirement should be done by independent investigators in order to reproduce this work.
