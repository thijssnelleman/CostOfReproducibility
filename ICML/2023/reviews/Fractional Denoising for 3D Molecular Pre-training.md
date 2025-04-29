
## Fractional Denoising for 3D Molecular Pre-training
Shikun Feng, Yuyan Ni, Yanyan Lan, Zhiming Ma, Wei-Ying Ma
Keywords: 
ICML/2023/Proceedings/24062 - Fractional Denoising for 3D Molecular Pre-training.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors release their implementation online (https://github.com/fengshikun/Frad). It has instructions for pretraining, downloadlinmks for pretrained models, instructions on how to finetune the model. There is an environment file for installation. Code has an acceptable amount of comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three datasets for which they provide citations and descriptions. There are automatic downloaders in the implementation (direct links).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in table 9, 10 and 11 of the appendix. They refer to a link online regarding some policy choices for training. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use MAE as a metric. Results are single runs. One data set is designated as pretraining dataset. The other have static splits for training and testing.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on molecular tasks and fractional denoising.
