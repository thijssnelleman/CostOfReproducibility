## Analytic-DPM: an Analytic Estimate of the Optimal Reverse Variance in Diffusion Probabilistic Models
Fan Bao, Chongxuan Li, Jun Zhu, Bo Zhang
Keywords: 
Award: Outstanding Paper Award
ICLR/2022/Proceedings/1087 - Analytic-DPM: an Analytic Estimate of the Optimal Reverse Variance in Diffusion Probabilistic Models.pdf
Project URL: https://openreview.net/attachment?id=0xiJLKH-ufZ&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation and pre-trained models in the reproducibility statement (https://github.com/baofff/Analytic-DPM). The authors state in the readme a small intro about what can be reproduced with the repository, the installation requirements, how to run various experiments, where to find pretrained models and checkpoints used for the study, and links to other implementations used as a basis or for inspiration. The repository is quite large and lacks an index. The code also contains fewer comments than preferred, but the most crucial parts seem to be well documented. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use CIFAR10, CelebA, ImageNet and LSUN bedroom for their experiments and provide citations for all. Summaries about the datasets are missing. The authors mainly use models pretrained on these datasets (links provided in implementation), but also train two themselves (links provided). As these are used as actual input to conduct the experiment on, the information on the datasets themselves is less important. Some key details on these models are provided in appendix F. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors conduct extensive theoretical analysis on the variables of their method in section 3 and provide results under various settings.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure, under various timesteps K, the negative log likelihood of bits/dim and FID (Citation provided, very brief explanation). No variation/aggregation applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[8]

-
