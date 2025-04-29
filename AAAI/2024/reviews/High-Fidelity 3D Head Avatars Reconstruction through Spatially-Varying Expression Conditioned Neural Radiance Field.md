
## High-Fidelity 3D Head Avatars Reconstruction through Spatially-Varying Expression Conditioned Neural Radiance Field
Minghan Qin, Yifan Liu, Yuelang Xu, Xiaochen Zhao, Yebin Liu, Haoqian Wang
Keywords: CV: 3D Computer Vision, CV: Applications
AAAI/2024/Proceedings/28505 - High-Fidelity 3D Head Avatars Reconstruction through Spatially-Varying Expression Conditioned Neural Radiance Field.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a source for their implementation (https://github.com/minghanqin/AvatarSVE). However, the repository states that 'Due to existing copyright restrictions and legal considerations, we are currently unable to open source the code for this project.'. This makes the statement in the paper misleading. The authors provide a general overview of their method with an example in the paper. Secondly, they give a larger but still high level overview of the method's framework. There are some notes about pre-processing in the experiments section, but any other details on the implementation is missing.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/3)

The authors use one private data set and provide some details on its collection. For comparability the authors cite two different public data sets that they evaluate on. There are some notes on pre-processing. No statistics are given on the public or private data sets to clarify comparability.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors introduce various parameters on their method in the Methods section but asside from a small ablation study where they omit (parts of) their method to create baselines, no real details are given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they produce quantative results on nine subjects and average them. This seems relatively straight forward given the task.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

The method aims to reconstruct three dimensional heads of avatars by applying computer vision. The specific technique presented is quite complex and the data handling is not easy either. The absence of implementation details and the private data set worsen this. In order to reproduce this paper, one would require significant experience, or major resources.
