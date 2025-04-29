
## 3DB: A Framework for Debugging Computer Vision Models
Guillaume Leclerc, Hadi Salman, Andrew Ilyas, Sai Vemprala, Logan Engstrom, Vibhav Vineet, Kai Xiao, Pengchuan Zhang, Shibani Santurkar, Greg Yang, Ashish Kapoor, Aleksander Madry
Keywords: 
NeurIPS/2022/Proceedings/54863 - 3DB: A Framework for Debugging Computer Vision Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation in footnote 1 (https://github.com/3db/3db). In the readme they statea link to installation instructions, a link to a demo, have a full documentation website on the code and a download link for data to use for reproduction. Overview given in figure 3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors provide a download link to data in their implementation. The authors state they created a dataset in 3.1. by downloading 408 instances from hdrihaven.com. They state what parts of the instances they used. This dataset has been matched to ImageNet classes. In appendix F they provide more details. ImageNet is only cited. The authors also use YCB dataset which they cite, but no other information except for a brief description.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors test pretrained models in their framework. No configurations applicable.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use accuracy as metric. Evaluations are over full datasets as specified. The aggregation/variation is over the datasets instances. Aggregation is averaging.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on CV, 3D CV and model debugging.
