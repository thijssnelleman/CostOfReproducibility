## Finetuning Text-to-Image Diffusion Models for Fairness
Xudong Shen, Chao Du, Tianyu Pang, Min Lin, Yongkang Wong, Mohan Kankanhalli
Keywords: 
ICLR/2024/Proceedings/18085 - Finetuning Text-to-Image Diffusion Models for Fairness.pdf
Project URL: https://openreview.net/attachment?id=hnrB5YHoYu&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

Authors provide a project URL in the abstract where the implementation repository is linked (https://github.com/sail-sg/finetune-fair-diffusion). Readme has overview of the method, installation instructions, where to download data, overview of the experiments directories which have their own readmes with example code how to run. In general the structure is large but well documented. Decent comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

CelebA, FairFace both cited. Link in repo. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Repository has a directory per experiment and each has its own detailed config files. Also described in text in appendix A. No acquisition specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Metrics explained in 5.1. Agg/var not clear. Data set up given in appendix A.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
