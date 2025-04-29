
## ShareBERT: Embeddings Are Capable of Learning Hidden Layers
Jia Cheng Hu, Roberto Cavicchioli, Giulia Berardinelli, Alessandro Capotondi
Keywords: NLP: (Large) Language Models, CSO: Constraint Optimization
AAAI/2024/Proceedings/31348 - ShareBERT: Embeddings Are Capable of Learning Hidden Layers.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present their implementation on a publicly available source (Github) (https://github.com/jchenghu/sharebert), how to run their code, and pretrained models. The authors provide clear mathematical documentation and illustrations of their method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors provide links to the pretrained models. The authors reference which source of data they use for training, but lack details/specifications of the data set which can lead to problems. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors define various hyperparameter regarding their model architectures and motivate them through ablation analysis, but many hyperparamters seem to be missing. There is no budget specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are clearly explained and defended. The authors explain the parametrization of the experiments including the ablation anaylsis.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The presented method requires a certain level of understanding of LLMs and the evaluation metrics used in the field in order to understand the work. However, due to the full documentation including their specified GitHub page, I believe this is substantially lower as it gives concrete examples.
