## A Conditional Point Diffusion-Refinement Paradigm for 3D Point Cloud Completion
Zhaoyang Lyu, Zhifeng Kong, Xudong XU, Liang Pan, Dahua Lin
Keywords: 
ICLR/2022/Proceedings/7026 - A Conditional Point Diffusion-Refinement Paradigm for 3D Point Cloud Completion.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in a footnote on the first page (https://github.com/ZhaoyangLyu/Point_Diffusion_Refinement). The readme contains an overview of the method, how to install the requirements, how to preprocess the data, how to run training and modify the settings, how to get output samples for analysis, and acknowledgement for inspiration by linking another repo. The comments are good. Structure is very large and can use an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three datasets: MVP, MVP-40 and Completion3D. Citations are provided and each is described, with great detail in appendix B. A link is given in the implementation for MVP, but for Completion3D it seems a bit more complicated.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The implementation contains various structured settings files used for the experiments, and it seems clear how to match which to which. The authors define a linear schedule for part of the hyperparameters in appendix A.1. Not all HP values are motivated there.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors define the evaluation metrics in 5.2. Results are single run. There is note of a training and test set in the paper (appendix) but not how this is done.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
