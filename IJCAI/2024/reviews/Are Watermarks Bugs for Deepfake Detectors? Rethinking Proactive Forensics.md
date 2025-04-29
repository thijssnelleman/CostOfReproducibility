
## Are Watermarks Bugs for Deepfake Detectors? Rethinking Proactive Forensics
Xiaoshuai Wu, Xin Liao, Bo Ou, Yuling Liu, Zheng Qin
Keywords: Multidisciplinary Topics and Applications: MTA: Security and privacy, Computer Vision: CV: Biometrics, face, gesture and pose recognition
IJCAI/2024/Proceedings/0673 - Are Watermarks Bugs for Deepfake Detectors? Rethinking Proactive Forensics.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their code and supplementary material online (https://github.com/sh1newu/AdvMark). The authors state some updates regarding their finetuned model and link it, note that the code is incomplete and that it (in part) only serves for refences and expect independent investigators to be able to implement it based on this. They provide direct links to the data sets / models. The code is largely without comments and seemingly unstructured. This means it will be a serious effort for independent investigators to follow the flow of the process to re-implement it.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide a direct link to the data and 'detectors' in their implementation documentation. The authors create/prepare a data set by using a public data set (which they cite) and explain the process on how they produce the dataset and divide it into training/testing. This processed data set is available online.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The auhtors state they use the hyperparameter settings for the pretrained models of their pipeline by following the original implementations. A few other hyperparameters regarding the finetuning are stated. The implementation uses yaml files to load the configurations, but these files are not given. This means many details regarding the hyperparameters in the pipeline need to be reverse engineered. No details regarding acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the training/testing split in the data (static) in 5.1, as an official split. The authors specify the evaluation metric with a formula and explanation. The results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience with the task and SOTA as many other works are used / applied from the field, as well as adversarial attacks.
