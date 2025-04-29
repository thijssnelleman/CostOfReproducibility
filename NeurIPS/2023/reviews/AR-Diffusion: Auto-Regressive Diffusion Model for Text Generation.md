
## AR-Diffusion: Auto-Regressive Diffusion Model for Text Generation
Tong Wu, Zhihao Fan, Xiao Liu, Hai-Tao Zheng, Yeyun Gong, yelong shen, Jian Jiao, Juntao Li, zhongyu wei, Jian Guo, Nan Duan, Weizhu Chen
Keywords: 
NeurIPS/2023/Proceedings/73068 - AR-Diffusion: Auto-Regressive Diffusion Model for Text Generation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their code in the abstract (https://github.com/microsoft/ProphetNet/tree/master/AR-diffusion). In the readme they state an overview on the method, how to install, where to download the dataset, how to train and infer, and evaluate with lopts of details. They also acknowledge other repos they build upon. Code needs more comments and repo is huge so an index is needed.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

Authors provide a download link in the implementation. The authors use GLEGE (direct link in footnote 6), XSUM (citation) and CNN/DailyMail (Citation) for text summarization, IWSLT data set (link it footnote 7) and CommonGen (link in footnote 8). XSUM, and CNN/DM are available in the readme link. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The HP values are summarised per dataset in table 8 and the architecture and other details in appendix B. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state the metrics used with citations in appendix B. Results are single model or average of 10. The authors present the result on the test set of each data set and in the appendix they seem to imply this is static/provided but is not actually explicitly stated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on diffusion models and text generation.
