## Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction
Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, Abdelrahman Mohamed
Keywords: 
ICLR/2022/Proceedings/6707 - Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/facebookresearch/av_hubert). In the readme they give an introduction to the method, links to download model checkpoints, a link to a demo on google colab, how to install the requirements, how to load a model, examples how to train a model, and how to run inferences. The code varies alot in comments, although the main methods seem to be well documented. structure is overseeable.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use LS3 and VoxCeleb2 and provide citations on the datasets, and a description of how they are used in 4.1. They provide preprocessing scripts and download links in the implementation. Extensive details on the datasets are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide extensive configuration files in the implementation. They state in appendix B.1. how they used the data for hyperparameter tuning. The grids are specified in B.4.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure WER (Not clarified) on the static test sets. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
