
## DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models
XiMing Xing, Chuang Wang, Chuang Wang, Haitao Zhou, Jing Zhang, Qian Yu, Dong Xu
Keywords: 
NeurIPS/2023/Proceedings/72425 - DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models.pdf
Project URL: https://ximinng.github.io/DiffSketcher-project/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their project page in the abstract wher they link their implementation (https://github.com/ximinng/DiffSketcher). In the reaadme they state example output, updates, installation instructions, a quick start for multiple specific cases with code and parameter explanations, acknowledgement of repositories they build upon. The code has very good comments. The repository tsructure is very large, and could use an index. Overview on the method is given in figure 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors do not train on a dataset, instead they employ a pretrained diffusion model and define their method over it. The pretrained model is automatically downloaded in their code and is cited in the paper. Statistics (as specified in the guidelines) do not apply in this setting.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state a hyperparameter in equation 5 (function w(t)) which they set to 100 according to a previous work. No other HPs.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors describe the quantitative evaluation metrics and motivate them in 5.2. and describe them extensively in appendix H with citations. The results presented are over four prompts in figure 6. The other results are qualitative (not applicable). No aggregation or variance applicable. No data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on diffusion models and CV optimisation.
