
## UKnow: A Unified Knowledge Protocol with Multimodal Knowledge Graph Datasets for Reasoning and Vision-Language Pre-Training
Biao Gong, Shuai Tan, Yutong Feng, Xiaoying Xie, Yuyuan Li, Chaochao Chen, Kecheng Zheng, Yujun Shen, Deli Zhao
Keywords: 
NeurIPS/2024/Proceedings/97740 - UKnow: A Unified Knowledge Protocol with Multimodal Knowledge Graph Datasets for Reasoning and Vision-Language Pre-Training.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors mainly publish a dataset. However they also produce baselines in sec 4. This implementation is not given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors present a new dataset and refer to appendix A on how to acquire it with link. Statistics given in table 2,3 and 4. Acquisition is detail in section 2 and visualised in figure 2 and 3.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

HPs are given in table 13 and 14 for each experiment. Acquisition not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The experiments are detailed in appendix C. with metric explanation and data set details. Experiments are repeated five times and they use mean + variance. Metrics are reported on validation and test sets, and data splits are given in table 4.  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on graph data and geometrical deep learning.
