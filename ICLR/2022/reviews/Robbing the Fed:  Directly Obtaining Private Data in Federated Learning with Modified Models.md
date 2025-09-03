## Robbing the Fed:  Directly Obtaining Private Data in Federated Learning with Modified Models
Liam H Fowl, Jonas Geiping, Wojciech Czaja, Micah Goldblum, Tom Goldstein
Keywords: 
ICLR/2022/Proceedings/7067 - Robbing the Fed:  Directly Obtaining Private Data in Federated Learning with Modified Models.pdf
Project URL: https://openreview.net/attachment?id=fwzUgo0FM9v&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a repository for their implementation, bareboness, in the reproducibility statement (https://github.com/lhfowl/robbing_the_fed) as well as a larger one (https://github.com/JonasGeiping/breaching). In the readme they state installation requirements and which notebook serves as an example to get up and running. The notebook is well documented and easy to follow. The code has decent comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use ImageNet and motivate their choice and provide a citation. Statistics provided in the appendix. Dataset downloads automatically in the code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors use a model from another work with its presented settings from there. Other parameters documented in the code, but not specific to the method.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure Identification (IIP, named and cited but not fully explained) success vs bin size over various batch sizes.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
