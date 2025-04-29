
## RSPT: Reconstruct Surroundings and Predict Trajectory for Generalizable Active Object Tracking
Fangwei Zhong, Xiao Bi, Yudi Zhang, Wei Zhang, Yizhou Wang
Keywords: CV: Vision for Robotics & Autonomous Driving, CV: Motion & Tracking, CV: Multi-modal Vision
AAAI/2023/Proceedings/25482 - RSPT: Reconstruct Surroundings and Predict Trajectory for Generalizable Active Object Tracking.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide two github sources of implementations they use, one for baselines comparison the other for their trajectory prediction module, but provide no other source of their own than their project website (https://sites.google.com/view/aot-rspt) which does not provide an implementation source. They do provide an extensive overview of the framework, examples of the problem, and step wise explanation of their method but no details whatsoever on how it was implemented, thus making it nearly impossible to reproduce.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(0/7)

The authors apply their method on 7 simulated environments from a different source which they cite. However the authors do not clearly state whether this is an openly available method or not. This can be determined by tracing the cite however, but relying on just the authors documentation this is unclear. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There is no mention of algorihm configurations, architectures, or hyperparameters at all.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The evaluation metrics are clearly explained regarding the environments and over what sequence they are collected. They also clearly state how many episodes are run for each method, which they average. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

The method deals with three dimensional reconstructions and object tracking for reinforcement learning. The implementation documentation is not present and neither are the hyperparameters. This makes reproduction extremely costly, as it is a very complex method and thus a lot of expertise (including practical) would have to be acquired in order to do so. Better documentation could have substantially lowered this cost.
