
## BARET: Balanced Attention Based Real Image Editing Driven by Target-Text Inversion
Yuming Qiao, Fanyi Wang, Jingwen Su, Yanhao Zhang, Yunjie Yu, Siyu Wu, Guo-Jun Qi
Keywords: CV: Computational Photography, Image & Video Synthesis, CV: Applications, CV: Language and Vision, CV: Multi-modal Vision
AAAI/2024/Proceedings/28503 - BARET: Balanced Attention Based Real Image Editing Driven by Target-Text Inversion.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not seem to link any repository of their original implementation. They do state various design choices and model sources in their implementation section. The authors also provide us with some pseudo code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use image data from a public dataset (Tedbench) as input and apply various models to it and do a user study on the results. The input data acquisition seems straight forward, but if collecting the exact same input images this may take some work. Doing a user study requires some effort, but it is not straight forward how many users would be required (62?) to do a similar study.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors provide the values of key hyperparameters of their method, and although some could be missing they do clearly state its based on stable diffusion. It is however unclear how these HP's were found and with what budget or how selection was done.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors specify clearly how the user study was conducted, except for how many participants were in the study ("62 valid results")

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The presented method is well presented with good examples, and the experiment seems relatively straight forward. However, the lack of code and details requiring model selection before conducting the user study could pose significant problems.
