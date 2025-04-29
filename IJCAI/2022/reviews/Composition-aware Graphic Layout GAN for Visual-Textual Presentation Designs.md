
## Composition-aware Graphic Layout GAN for Visual-Textual Presentation Designs
Min Zhou, Chenchen Xu, Ye Ma, Tiezheng Ge, Yuning Jiang, Weiwei Xu
Keywords: Application domains: Images and visual arts, Methods and resources: Machine learning, deep learning, neural models, reinforcement learning
IJCAI/2022/Proceedings/0692 - Composition-aware Graphic Layout GAN for Visual-Textual Presentation Designs.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors provide a link for their implementation (https://github.com/minzhouGithub/CGL-GAN). The readme states it will be released soon, otherwise its empty. The authors state in 6.1 they use PyTorch as a framework/library for their implementation. A framework figure is presented in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(0/1)

The authors state they collect data from e-commerce platforms in section 3. A brief description is given and a sample presented in figure 1, and some examples on the data in the other figures as well. The authors state a few statistics on the dataset (size, training/testing size). The data structure is also discussed in section 3 and the categories. The exact sources are not given and the data is not available (Should be in the empty implementation repository).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparameter values in section 6.1. A full HP space summary is missing. As there is only one dataset experiment, the values are clear for each experiment. There is no acquisition strategy or budget specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors conduct a user study and is described in detail in section 5. Then the metrics are described and explained in details, which the authors introduce due to 'no existing ... relevant measures for poster layouts'. Citations are provided where relevant. The train/test split is provided in section 3. The results are single runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries experience in CV and generative AI. Especially since new concepts are introduced in this paper (new metrics, new task, new data set), pratical experience is need as well as with related work on the paper to grasp the task. The missing implementation substantially worsens this, as there is less documentation to work with and no data set (for a new task)
