## Quantized Compressed Sensing with Score-Based Generative Models
Xiangming Meng, Yoshiyuki Kabashima
Keywords: 
ICLR/2023/Proceedings/11274 - Quantized Compressed Sensing with Score-Based Generative Models.pdf
Project URL: https://openreview.net/attachment?id=OOWLRfAI_V_&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/mengxiangming/QCS-SGM). In the readme they stayed how to install, how to use the code with explanation of the parameters of the main entry points, where to find the configuration files and how to use, structure of the repository, where to find checkpoints and link a repo they build upon. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use MNIST, CIFAR-10 and CelebA, provide citations and the code automatically download CIFAR10, LSUN, MNIST and CelebA. Details are given in section 4. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors list hyperparameter values in text in appendix F. Structured files containing the values are available per dataset in the configuration. Acquisition they partially refer to a previous work but its not clarified for all.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[5]

The authors measure PSNR, SSIM (stated in 4.1) but its not always clear what the aggregation and variation are on. Data split also not always clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
