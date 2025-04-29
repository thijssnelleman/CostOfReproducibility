
## Detecting Out-of-distribution Data through In-distribution Class Prior
Xue JIANG, Feng Liu, zhen fang, Hong Chen, Tongliang Liu, Feng Zheng, Bo Han
Keywords: 
ICML/2023/Proceedings/24725 - Detecting Out-of-distribution Data through In-distribution Class Prior.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their code (https://github.com/tmlr-group/class_prior). In the readme they state installation instruction, how to download and prepare the dataset and how to run the code to reproduce their results. The code base is small and the comments are acceptable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors provide data set download instructions in the implementation. The authors construct an imbalanced subset and explain how in section 4.1. On the original they provide a citation. Other details not specified. The authors use four data sets (or subsets thereof) for testing. They provide the same information on each.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors link a repository regarding model training. These trained models are then used as input for their method. This has a few paramaeters as can be seen in test_ood.py's arguments. Some of these values are specified in 4.1. A full summary on this is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use AUROC and FPr95 as metrics which are fairly standard and explained under table 1. The results are per model/configuration. Test sets are seperate data sets.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on OOD learning.
