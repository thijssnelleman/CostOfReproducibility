
## HVOFusion: Incremental Mesh Reconstruction Using Hybrid Voxel Octree
Shaofan Liu, Junbo Chen, Jianke Zhu
Keywords: Robotics: ROB: Localization, mapping, state estimation, Computer Vision: CV: 3D computer vision, Computer Vision: CV: Applications, Robotics: ROB: Robotics and vision
IJCAI/2024/Proceedings/0757 - HVOFusion: Incremental Mesh Reconstruction Using Hybrid Voxel Octree.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/Frankuzi/HVOFusion). In the readme they provide an introduction to the method with an architecture illustration, installation details, dataset download links and how to place the data into the implementation, how to run the code with different configurations and where the results can be found. The authors provide configuration files for all parameters in the config directory. The code has very descriptive comments. They dedicate an implementation section with some more details.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors provide a download link to 'dataset' in their implementation documentation. In 4.1 they describe the data sets used with citations and descriptions. No statistics are provided. It is not clear if they provide a download for all the datasets, but this could be easily checked.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide configuration files in their implementation documentation. The authors discuss HP values in the implementation section. No details are given on how these values were acquired. The authors also present a modular ablation study in table 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics used in 4.2 (which are standard,they also explain how they are computed) and 4.3, where they cite sources for but no explanations. There are no details stated regarding training/testing set but the procedure does seem to imply there is some training procedure done. Perhaps this requires more task/field specific expertise to determine. The results indicate single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a thorough understand of CV/3D reconstruction.
