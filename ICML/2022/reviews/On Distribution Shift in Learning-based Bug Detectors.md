
## On Distribution Shift in Learning-based Bug Detectors
Jingxuan He, Luca Beurer-Kellner, Martin Vechev
Keywords: 
ICML/2022/Proceedings/18391 - On Distribution Shift in Learning-based Bug Detectors.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/eth-sri/learning-real-bug-detector). In the readme they state installation instructions, how to download the data, the structure of the code with the downloaded files, how to execute the code with arguments explanation, and various options on constructing your own dataset. The code can use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors construct their own dataset. They publish a link to it in their implementation including code it was used to construct with links to the original source input. Construction is overviewed in figure 4. Statistics are available in table 1. The dataset construction is described in section 4.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters with an overview in table 9 per experiment. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are described in section 5. The authors have a seperate test set in their data set. The results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on bug detection in code and distribution shift.
