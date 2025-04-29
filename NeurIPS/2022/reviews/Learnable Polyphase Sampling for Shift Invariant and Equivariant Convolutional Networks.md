
## Learnable Polyphase Sampling for Shift Invariant and Equivariant Convolutional Networks
Renan A. Rojas-Gomez, Teck-Yian Lim, Alex Schwing, Minh Do, Raymond A. Yeh
Keywords: 
NeurIPS/2022/Proceedings/54728 - Learnable Polyphase Sampling for Shift Invariant and Equivariant Convolutional Networks.pdf
Project URL: https://raymond-yeh.com/learnable_polyphase_sampling/ 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the project page (https://github.com/raymondyeh07/learnable_polyphase_sampling). In the readme they state installation instructions, demo instructions, where to download data and where to find the results, and acknowledge a few repos they used for their implementation. The code has okay comments. Structure is doable due to good file/dir names and explained in the appendix.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use CIFAR-10, ImageNet and PASCAL VOC as datasets. Citations provided. Data downloads automatically in the implementation. No descriptions/statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are specified in appendix A4. Full config files per experiment available in the implementation. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metrics are top-1 accuracy and s/C-cons defined in section 5. Results are applying the method over single models except for table 1 where they report mean + std dev over 5 runs with different inits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on shift invariance.
