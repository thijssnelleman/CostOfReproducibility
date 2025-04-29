
## ReMoNet: Recurrent Multi-Output Network for Efficient Video Denoising
Liuyu Xiang, Jundong Zhou, Jirui Liu, Zerun Wang, Haidong Huang, Jie Hu, Jungong Han, Yuchen Guo, Guiguang Ding
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/20182 - ReMoNet: Recurrent Multi-Output Network for Efficient Video Denoising.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a source to the implementation. The implementation details section provide information regarding their method input size and architecture. They refer for more details to the supplementary material, which is not present (AAAI limitations). The authors do provide extensive illustrations on their method, including examples.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(2/2)

The authors use two benchmark data sets and provide a small description on them. No citations are provided, nor a direct link. Minor information is provided on the details of the data set. A lot is left to independent investigators to find out, but supposedly (since they state they are benchmark datasets) it should not a too high effort to acquire the data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors state for their baseline method 'hyperparameters are tuned on target data sets'. A few parameter values are given in the implementation details. No other details are given, except a reference to the non-present supplementary material.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors state they use Davis-train data set for training, and show results in table 3 on davis test. They provide results on set8 in table 4, implying that they did not use any of set8 for training. They state 4 metrics, one of which is straight forward, another which they briefly describe (and is clear) but the first two are only given as acronyms requiring subfield knowledge to understand or should be researched. Results imply single runs/models.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a thorough understanding of Computer Vision to understand the method being presented, but as well for the experiment being conducted.
