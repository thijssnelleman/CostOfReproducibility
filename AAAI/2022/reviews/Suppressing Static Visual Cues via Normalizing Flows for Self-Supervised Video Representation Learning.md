
## Suppressing Static Visual Cues via Normalizing Flows for Self-Supervised Video Representation Learning
Manlin Zhang, Jinpeng Wang, Andy J. Ma
Keywords: Computer Vision (CV), Machine Learning (ML)
AAAI/2022/Proceedings/20239 - Suppressing Static Visual Cues via Normalizing Flows for Self-Supervised Video Representation Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide a source for their implementation. A large training pipeline schematic is given. The authors provide details on their implementation regarding the 'flow model' and provide a citation, and two backbone networks. They refer to the supplementary for more details, but this is not present (AAAI limitations). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/4)

The authors use 4 data sets (3 sources, one of them is a subset of another) for their experiments and provide citations on them. No other details are given but based on the citations they are seemingly public.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors provide a few key hyperparameter values and architecture size values, both in text and table 1. It is hard to determine if all needed values are presented. The authors do not specify an acquisition method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors state the training procedures and how the evaluation is done including metric aggregation. There is no clear definition of a training/testing set. This either takes more expertise to determine or is not clearly explained. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires a good understanding of computer vision to understand the method and presented experiments.
