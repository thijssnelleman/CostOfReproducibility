
## G2P-DDM: Generating Sign Pose Sequence from Gloss Sequence with Discrete Diffusion Model
Pan Xie, Qipeng Zhang, Peng Taiying, Hao Tang, Yao Du, Zexian Li
Keywords: CV: Computational Photography, Image & Video Synthesis
AAAI/2024/Proceedings/28860 - G2P-DDM: Generating Sign Pose Sequence from Gloss Sequence with Discrete Diffusion Model.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors provide a github link (https://slpdiffusier.github.io/g2p-ddm) but only demonstrate more examples here. The authors do note that implementation details should be included in the Appendix but this is not available on AAAI. The Arxiv version seemingly does not contain this information either. A quick google search does produce a github repository seemingly associated with the work, but this should be provided by the authors. The paper has visualisations of the method, which should help with re-implementation. This cost could have been lowered by correctly linking / stating the implementation source.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use a publicly available data set with citation, and even state that this is the only publicly available data set for their task. The authors provide meta information on the data. They also clarify how ground truth was extracted from the data but with the lack of implementation documentation this does increase the cost.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state that the appendix should contain a full documentation on the hyperparameters but this is nowhere to be found (AAAI does not allow it and the Arxiv version lacks one as well). There are some hyperparameters documented in the paper, mainly regarding the architecture. No details on how these were found are provided. This cost could possibly have been lowered by providing the appendix referenced.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the used metrics and their motivation. From the data details the authors seem to suggest only one shot on the test set is used for the procedure, but its not specifically stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The work deals with generating pose sequences from gloss sequences. A good understanding of discrete diffusion should be expected by the independent investigators. The lack of implementation details severly increase this threshold, as many details would have to be researched by the independent investigators.
