
## Contrastive Energy Prediction for Exact Energy-Guided Diffusion Sampling in Offline Reinforcement Learning
Cheng Lu, Huayu Chen, Jianfei Chen, Hang Su, Chongxuan Li, Jun Zhu
Keywords: 
ICML/2023/Proceedings/24092 - Contrastive Energy Prediction for Exact Energy-Guided Diffusion Sampling in Offline Reinforcement Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/thu-ml/CEP-energy-guided-diffusion). In the readme they provide results from the paper and an overview of the repository structure. There is a second readme detailing how to run the code for three experiments, they also link pretrained models. The code has an acceptable amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use various public environments which they provide citations on, code is available for in the implementation, parameter values are specfied in appendix I.2., but only brief descriptions are given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

There are a few mentions of hyperparameters in the appendix. In I.2. a grid for hyperparameter s is specified with a grid search per environment. The selected values are reported in table 5. The other mentioned hyperparameters aren't discussed and in the code there also seems multple hyperparameters at play. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors run all experiment for 5 trials and reporte the mean + std dev, where each trials consists of collecting the result over 10 or 100 seeds (Appendix I.2.). The reported results are normalized. The metric is seemingly environment related but its not stated in 5.4.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience in offline reinforcement learning.
