
## Flow-Based Unconstrained Lip to Speech Generation
Jinzheng He, Zhou Zhao, Yi Ren, Jinglin Liu, Baoxing Huai, Nicholas Yuan
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/19966 - Flow-Based Unconstrained Lip to Speech Generation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation, only a link to a demo video. The authors cite a layer from a previous work they used to implement their method. They state their implementation is based on PyTorch. The authors provide a large archticture schematic (figure 2). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use public dataset and provide a description, citation, preprocessing steps and a single statistic on them. More information would be welcome and a direct link to where it can be found, which could have been included on the demo website.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The author refer to part of their configuration to a previous work, and in part provide the hyperparameters. It requires some effort to verify all needed values are given in part due to the missing implementation. No details are provided on the acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors state metrics used and provide citations on them, but there is no explanation/details given. The authors also do human evaluation and provide the metric used but no description on it. They do cite the metrics/procedure used for this human evaluation. The authors do not specify how the data was divided into training/testing sets. The result tables seem to indicate single run/model results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP, computer vision, and the specific task at hand to understand the objectives/metrics used. 
