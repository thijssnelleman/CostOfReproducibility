## ExT5: Towards Extreme Multi-Task Scaling for Transfer Learning
Vamsi Aribandi, Yi Tay, Tal Schuster, Jinfeng Rao, Huaixiu Steven Zheng, Sanket Vaibhav Mehta, Honglei Zhuang, Vinh Tran, Dara Bahri, Jianmo Ni, Jai Gupta, Kai Hui, Sebastian Ruder, Donald Metzler
Keywords: 
ICLR/2022/Proceedings/7043 - ExT5: Towards Extreme Multi-Task Scaling for Transfer Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors state the code is already mostly opensourced (Regarding ExT5 and T5^2) and provide citations and links, and their new model ExT5 is placed in a public library (https://github.com/tensorflow/mesh) which is well documented. However, they do not seem to provide their own code for the study. Although these serve as good starting points, some work is needed to reconstruct for analysis. However, their main contribution is dataset ExMix, but section 3 is mainly dedicated on measuring the performance of these previous works on their new dataset.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(44/44)

The authors present a new dataset, ExMix, which is a collection of tasks which consists of 44 public datasets. ExMix is well documented, with statistics, descriptions and citations on all in table 11. They report results on SuperGLUE (Table 5), GEM (Table 6), Rainbow (Table 7), MsMarco (Table 8) and CBQA datasets (Table 9). However, a clear link to the dataset, or the publicly available datasets seems to be missing so some reconstruction will be in order.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

There are mentions of hyperparameter R with various values in the text, and there are some notes in 3.1 regarding learning rates and architectures. More details are given in appendix B.2. how the learning rates were acquired (grid search). Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report the results on specified splits per table, and measure METEOR, ROUGE-2, BLUE, MRR@10 but most metrics remain un explained. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
