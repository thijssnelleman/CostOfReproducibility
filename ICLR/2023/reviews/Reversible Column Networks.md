## Reversible Column Networks
Yuxuan Cai, Yizhuang Zhou, Qi Han, Jianjian Sun, Xiangwen Kong, Jun Li, Xiangyu Zhang
Keywords: 
ICLR/2023/Proceedings/11922 - Reversible Column Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors state the implementation link in the abstract (https://github.com/megvii-research/RevCol). In the readme the authors state updates, a model zoo with details/downlood links, a link to a seperate getting started readme where they detail how to install/prepare data/how to run code with example parameter values, acknowledgements for other repos, contact details. Structure is huge and needs an index. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

ImageNet, MS-COCO, ADE20k (cited not described). Authors refer to previous work for download links of the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors provide configuration files per experiment in the configs dir of the implementation. The authors refer to a previous work for their choice of settings, but why is not given. Overview given in appendix F.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors measure APbox APbox, 50 APbox, 75 APmask APmask, 50 APmask, 75 Params FLOPs. Results are single run. Data sets are split in their uses for the experiment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
