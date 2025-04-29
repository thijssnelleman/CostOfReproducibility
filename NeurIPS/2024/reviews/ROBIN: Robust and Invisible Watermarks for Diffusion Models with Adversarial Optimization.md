
## ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization
Huayang Huang, Yu Wu, Qian Wang
Keywords: 
NeurIPS/2024/Proceedings/95144 - ROBIN: Robust and Invisible Watermarks for Diffusion Models with Adversarial Optimization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the checklist (https://github.com/Hannah1102/ROBIN). In the readme they state installation instructions, how to run the code with some parameters and credits for an inspiration. The code has okay comments (some functions are completely without). There are quite a lot of files so an index is welcome.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors state the datasets used in 4.1. The Gustavosta dataset is cited and a direct link is in the references but no description or statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors note the hyperparameters in sec 4.1., state the hyperaparmeters of the method in algorithm 1, with its values in appendix A.3. The values were acquired experimentally for the latter, but no specification for the former. no budget. Structured overview in the code (config files) but unclear which belong to the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The evaluation metrics are described in 4.1. and are detailed in appendix B.1. The results are single model/run. The authors state the amounts of data the metrics are calculated over but not the source of the data thus data split is unclear. In table 4 the results are presented as average + std dev over 5 independent runs with different seeds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on diffusion models, watermark removal and adversarial training.
