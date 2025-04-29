
## Primitive-Based 3D Human-Object Interaction Modelling and Programming
Siqi Liu, Yong-Lu Li, Zhou Fang, Xinpeng Liu, Yang You, Cewu Lu
Keywords: CV: 3D Computer Vision, CV: Representation Learning for Vision
AAAI/2024/Proceedings/28323 - Primitive-Based 3D Human-Object Interaction Modelling and Programming.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state that the code and data can be found on their website (https://mvig-rhos.com/p3haoi). However, the referal link there to the GitHub yields a 404. High level choices can be found in the experiments section, after which the authors refer to the appendix which does not exist.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/1)

The authors present a new data set in their work, with extensive documentation on the creation method including annotation, synthesis and metrics. However, the provided link gives a 404 when trying to access the data. When released, this cost should in principle be a 1 instead.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

Hyperparameters of the two presented baselines are not noted in the paper, although the authors state "more settings are available in the appendix" which are absent. The implementation is also absent, so no back up source can be used to determine which hyperparameter values were used. The authors do cite which methods they modify to apply as baselines on their data set, which could be used to determine what kind of parameters are relevant.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors extensively describe the task at hand and the metrics that are to be evaluated, and analyse the quantative results. They are one shot evaluations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Significant expertise regarding human object interaction modelling is required in order to fully grasp the steps done regarding data set acquisition and synthesis. The absence of the data set and implementation documentation does not impact this evaluation.
