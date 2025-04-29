
## TFLOP: Table Structure Recognition Framework with Layout Pointer Mechanism
Minsoo Khang, Teakgyu Hong
Keywords: Computer Vision: CV: Recognition (object detection, categorization), Computer Vision: CV: Applications, Natural Language Processing: NLP: Applications
IJCAI/2024/Proceedings/0105 - TFLOP: Table Structure Recognition Framework with Layout Pointer Mechanism.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide the source of their implementation (https://github.com/UpstageAI/TFLOP). The readme has a short intro on the method with visualisation, updates list, how to install, how to download the data set / pretrained model and what the final directory structure should look like, data preprocessing instructions, and how to train/evaluate the method. The code has some comments but could use some more in some places. The repository directory structure is also rather large and could use some explanation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three public benchmark datasets, provide citations on them and lengthy descriptions with key statistics. Download instructions are given on the implementation docs.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the value of several hyperparameters in 4.2. However this does not seem to be complete and will have to be extracted from the implementation docs with some effort. No details specified on how this was acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors describe their evaluation metrics in detail in 4.3. The train/test split is given for one data set, but for the other the training procedure is not clear and will require some effort to determine.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires a thorough understanding of the task, as the method presented is quite complex and uses many different ML techniques from different subfields.
