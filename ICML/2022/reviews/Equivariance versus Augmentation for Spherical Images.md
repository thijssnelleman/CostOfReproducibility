
## Equivariance versus Augmentation for Spherical Images
Jan Gerken, Oscar Carlsson, Hampus Linander, Fredrik Ohlsson, Christoffer Petersson, Daniel Persson
Keywords: 
ICML/2022/Proceedings/16211 - Equivariance versus Augmentation for Spherical Images.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their code online (https://github.com/JanEGerken/sem_seg_s2cnn). In the readme they state the source on which they build their implementation and the differences between them and how to cite the paper. The repository is installable (setup.py available) and the code has a lot of comments. The directory structure can use an index but it is overseeable enough with the naming scheme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two public datasets in their method. The authors have instructions on how to generate their dataset from the public data set in the implementation. The datasets download automatically. The authors discuss the dataset in length in 3.2. and 3.4. Citations on the original datasets are provided but only minor statistics given which is acceptable due to all the effort the authors put in to make their data publicly available. Data gneeration is also discussed in appendix C.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state architectures were randomly generated and they provide some details on this in section 3.1. More details can be found in B.1. and B.2. They generate 20 of these 'for each desired parameter range' and picked the best on a holdout set (random search). The table 4 & 5 shows the selected architecture. All other hyperparameters are set to a fixed value in appendix B which is not explained how they were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The experiments are evaluated on test accuracy for various model architectures and types over increasing number of training images. The data sets have static train test splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries experience in CV.
