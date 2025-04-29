
## Retrieval-Augmented Primitive Representations for Compositional Zero-Shot Learning
Chenchen Jing, Yukun Li, Hao Chen, Chunhua Shen
Keywords: CV: Language and Vision, CV: Image and Video Retrieval
AAAI/2024/Proceedings/28096 - Retrieval-Augmented Primitive Representations for Compositional Zero-Shot Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide no source for their implementation. They state in the experiments section that they created their implementation using PyTorch and they use an architecture from previous work. There is a general architecture schematic present in the paper (figure 3) and a large overview of the proposed method (figure 2), and an introductory fighure to the problem statement (figure 1). No other details regarding the implementation are given, still making this process extremely costly.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors evaluate their method on three datasets, which they name and cite sources for. There is a description on each data set and detailed statistics present. The authors state they are 'widely used' but no direct link is provided where they can be found. However, with the citations present, it should be little effort to find this source.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors give the set values for their loss hyperparameters and retireved images K for each data set. Various other values are given, but certain key values are missing such as the learning rate. The reconstruction of this can take time, especially with the absence of implementation. There are no details given on how the hyperparameter values were determined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors introduce their metrics in a separate section with details on their computation. Under their data set explanation the authors discuss the train/validation/testing splits. No ohter specific details are given by the authors, and the values in the results table seem to suggest single run results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The expertise required to reproduce this is mainly for the concepts of zero shot learning, although explained and introduced well with examples by the authors. Furhtermore, the absence of the implementation severely raises this cost, as independent investigators will have to reconstruct every detail along the way.
