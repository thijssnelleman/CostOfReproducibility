## Chain-of-Experts: When LLMs Meet Complex Operations Research Problems
Ziyang Xiao, Dongxiang Zhang, Yangjun Wu, Lilin Xu, Yuan Wang, Xiongwei Han, Xiaojin Fu, Tao Zhong, Jia Zeng, Mingli Song, Gang Chen
Keywords: 
ICLR/2024/Proceedings/18977 - Chain-of-Experts: When LLMs Meet Complex Operations Research Problems.pdf
Project URL: https://openreview.net/attachment?id=HobyL1B9CZ&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to the implementation in 4.2 (https://github.com/xzymustbexzy/Chain-of-Experts). Readme has installation instructions, explanation on how to run the code and its parameters, statement on two datasets and their availability. Comments are good. File structure is large and can use an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

LPWP (cited) and ComplexOR. Described in 4.1. First is present in the repo. Althoug hit is stated in the readme the latter is still under review, the raw data is present and they seem to have uploaded the processed version too albeit unclear. More details given in appendix A. Clarity on the dataset would be most welcome. The parameter of generation, as shown in figure 4 of the appendix, seem to be given in the config files of the implementation per dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The method has two parameters, N and T. Values given in text in 4.2. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors measure Accuracy↑ CE rate↓ RE rate↓ and explain them in 4.2. Results are over 5 runs averaged. Split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
