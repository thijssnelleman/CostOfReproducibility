
## Rethinking the Development of Large Language Models from the Causal Perspective: A Legal Text Prediction Case Study
Haotian Chen, Lingwei Zhang, Yiran Liu, Yang Yu
Keywords: General
AAAI/2024/Proceedings/31914 - Rethinking the Development of Large Language Models from the Causal Perspective: A Legal Text Prediction Case Study.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/Carrot-Red/Rethink-LLM-development). They document how to get the code to work with requirements, a source for the basis of their implementation, a data preprocess instruction, how to train the models and how to run the 'attacks' presented in the paper. They also include scripts to calculate the statistics. In general the code has descent amount of comments. The paper has an illustration how the method is positioned in the problem and a large illustration on the framework of the method. They also note some details on their implementation in the experimental settings section.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/2)

The authors use two data sets with clear descriptions and explanations, citations and statistics. The first data set has a download link to it in the implementation documentation, it is unclear whether the second one is (publicly) available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify the learning rate and the optimiser they use on the pre-trained models. Although there could be more HP's, these seem to be the key values needed. Other HP's could perhaps be extracted from the implementation if necessary with a bit of effort. It is unclear under what budget these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics used are clearly stated, and the evaluations are seemingly one run of 8 attacks. With the presence of the implementation documentation, with a bit of effort any other details should be easy to figure out.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The authors method is on adverserial attacks on LLM's. Although some experience is required, this is relatively low and should be accesible to many as the authors provide an introduction and examples to the concept.
