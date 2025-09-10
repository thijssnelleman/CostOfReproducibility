## Towards Offline Opponent Modeling with In-context Learning
Yuheng Jing, Kai Li, Bingyun Liu, Yifan Zang, Haobo Fu, QIANG FU, Junliang Xing, Jian Cheng
Keywords: 
ICLR/2024/Proceedings/19549 - Towards Offline Opponent Modeling with In-context Learning.pdf
Project URL: https://openreview.net/attachment?id=2SwHngthig&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation in the supplementary materials (https://openreview.net/attachment?id=2SwHngthig&name=supplementary_material). The readme has installation notes, where to download datasets and how to place them in the repository, how to run the code and configure the environments and methods. Code has almost no comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use Markov Soccer and Particleworld Adversary, both cited. They are described in appendix E. Download links in repository.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

HP values reported per stage in appendix J, in tables. The authors apply previous works within their method, thus sourcing the HPs from there as stated in appendix H. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure average environment return, reporting the average and standard error of the mean results over 5 random seeds. Split provided in the code.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
