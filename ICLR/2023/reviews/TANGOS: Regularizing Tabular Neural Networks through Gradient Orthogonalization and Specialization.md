## TANGOS: Regularizing Tabular Neural Networks through Gradient Orthogonalization and Specialization
Alan Jeffares, Tennison Liu, Jonathan Crabbé, Fergus Imrie, Mihaela van der Schaar
Keywords: 
ICLR/2023/Proceedings/11186 - TANGOS: Regularizing Tabular Neural Networks through Gradient Orthogonalization and Specialization.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide two links in footnote 1 and 2 of section 5, and finding that the second is a fork of the first, we use the first footnote as their implementation (https://github.com/alanjeffares/TANGOS). In the readme, they state a getting started including installation details, how to download datasets and configure them for the code, overview on the code file structure, how to run the code and a notebook demonstrating the code usage. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(19/20)

The authors use 20 tabular datasets from the UCI repository: Facebook, Boston, Weather, Wine Quality, Bio Concentraion, Skillcraft, Forest Fire, Protein, Student, Abalone, Heart, Breast, Cervical, Credit, HCV, Australian, Tumor, Entrance, Thoracic and Soybean. Details are provided with citation for each in table 8 of appendix L (includes more info), including 'deconstructed' links using IDs, which is explained in the implementation. The authors note one dataset has been removed due to ethical issues, technically making one private but this is fairly and clearly stated.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide configuration files containing HP values per experiment/dataset. In appendix B the authors state the hyperparameter grids they conducted a search over, which they validated on the validation set using three random seeds.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use cross validation with 80-20 split for each dataset. The authors measure MSE and NLL, using the average and presenting the standard error in table 6 over the 10 repeats.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
