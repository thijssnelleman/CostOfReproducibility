
## MULTISCRIPT: Multimodal Script Learning for Supporting Open Domain Everyday Tasks
Jingyuan Qi, Minqian Liu, Ying Shen, Zhiyang Xu, Lifu Huang
Keywords: NLP: Language Grounding & Multi-modal NLP, NLP: Generation
AAAI/2024/Proceedings/31487 - MULTISCRIPT: Multimodal Script Learning for Supporting Open Domain Everyday Tasks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors statte they provide a link to their code checkpoints and data sets on GitHub (https://github.com/VT-NLP/MultiScript). The Readme only provides a link back to the paper and a video source. It contains a very large data file (data_text.json, the presumably presented data set) and a license. The git ignore file seems to indicate there is more to it but simply not available. The authors present a schematic of the overall framework of the proposed tasks, but not much details are given on their implementations. The papers main concern is introducing their newly produced data set and provide baselines on them. Although the authors state they only use pretrained models, a lot of effort to reproduce these baselines is required with the absence of their implementations.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The paper introduces a new dataset and publishes it publicly on GitHub. The authors provide statistics and descriptions on the data set, and explain how it was sourced and created.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors take pre-trained models from other sources, without re-training, so hyperparameters are in this process not applied.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors explain and defend their selected metrics, and cite a source for them. They provide details on their human experiment set up. There is a long description on how the models are evaluated against the data.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[1]

It is an accesible paper, especially because they introduce many baselines they want to evaluate on their new data set.
