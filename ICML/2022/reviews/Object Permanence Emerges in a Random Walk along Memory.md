
## Object Permanence Emerges in a Random Walk along Memory
Pavel Tokmakov, Allan Jabri, Jie Li, Adrien Gaidon
Keywords: 
ICML/2022/Proceedings/16737 - Object Permanence Emerges in a Random Walk along Memory.pdf
Project URL: https://tri-ml.github.io/RAM/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide alink to their project page where they link their implementation (https://tri-ml.github.io/RAM/). In the readme they refer to installation instructions, data instructions on how to set this up and a readme for reproducing the experiments. They also explain that in one directory all scripts regarding the experiments can be found. The code needs more comments, and the repo structure is large so an index is nice to have as well. Pseudo code is available in algorithm 1. Implementation notes are given in 4.2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide links to download the datasets in the implementation. The authors use three data sets on which they provide citations, descriptions and some minor statistics in 4.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the training details in appendix A, but also state in section 4.2 that many values stay the same as a previous work. The authors also give the commands in the implementation for their experiments which provides some hyperparameter values. A full summary is missing. Acquisition not specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate using mean IoU over the LA-CATER test set, and validation sets of PD and KITTI. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience in Computer Vision.
