
## Unsupervised Multi-Exposure Image Fusion Breaking Exposure Limits via Contrastive Learning
Han Xu, Liang Haochen, Jiayi Ma
Keywords: CV: Computational Photography, Image & Video Synthesis, CV: Low Level & Physics-Based Vision, CV: Multi-modal Vision
AAAI/2023/Proceedings/25404 - Unsupervised Multi-Exposure Image Fusion Breaking Exposure Limits via Contrastive Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide a source for their implementation (https://github.com/hanna-xu/MEF-CL). However the link provides a 404 error. There are some details of the implementation given regarding the library (TensorFlow) and some data processing/selection. An overall framework schematic is presented with a good amount of details and some examples. The 404 error means it will be a lot of work for independent investigators to re-implement the method.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors state they do experiments on a public data set which they cite and provide a direct link to. The authors provide a description on the data set and some statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide hyperparameter settings in the implementation details. Due to the 404 error it is difficult to verify these are the only needed HP's. No details are given on how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Details regarding training and train/test splitting are provided. The metrics used are briefly described and sources cited where needed. It is not directly clear over what the mean and std dev are calculated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method requires a good understanding on computer vision. The absence/404 error of the implementation makes it harder to fully grasp the method. However the authors do provide clear documentation and a good number of examples. The level of expertise needed is in part also due to simply the high level of the method.
