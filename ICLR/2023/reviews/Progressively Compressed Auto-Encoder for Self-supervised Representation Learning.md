## Progressively Compressed Auto-Encoder for Self-supervised Representation Learning
Li Jin, Yaoming wang, XIAOPENG ZHANG, Yabo Chen, Dongsheng Jiang, Wenrui Dai, Chenglin Li, Hongkai Xiong, Qi Tian
Keywords: 
ICLR/2023/Proceedings/12083 - Progressively Compressed Auto-Encoder for Self-supervised Representation Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/caddyless/PCAE/). The readme has no details on how to install or run the code. The code has decent comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use ImageNet, COCO but provide no information.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

The authors refer to a previous work for Hp values for 'fair comparison'. The authors conduct an ablation study on the HPs in 4.3 over two parameters. Archtitecture and one HP value is provided in appendix B. Default HP values for models can be found in the code, and in some cases HP values are stated in tables, although no configuration files etc can be found to determine for all parameters which values were exactly used for the experiments.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure top-1 accuracy and use the validation set of ImgaeNet in a few cases. The authors state they pretrain on ImageNet. Results are single run. It is not completely clear what dataset splits are used, although this can perhaps be deduced from the code.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
