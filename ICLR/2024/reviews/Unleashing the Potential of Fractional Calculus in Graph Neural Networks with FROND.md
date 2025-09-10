## Unleashing the Potential of Fractional Calculus in Graph Neural Networks with FROND
Qiyu Kang, Kai Zhao, Qinxu Ding, Feng Ji, Xuhao Li, Wenfei Liang, Yang Song, Wee Peng Tay
Keywords: 
ICLR/2024/Proceedings/17486 - Unleashing the Potential of Fractional Calculus in Graph Neural Networks with FROND.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to the implementation in the abstract (https://github.com/zknus/ICLR2024-FROND). The readme has a table of contents, installation notes, how to run the code, acknowledgement of a repo used to build this one. Code has okay comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(18/18)

Cora Citeseer Pubmed CoauthorCS Computer Photo CoauthorPhy ogbn-arxiv Airport Disease, Politifact and Gossipcop, Roman-empire Wiki-cooc Minesweeper Questions Workers Amazon-ratings. Citations provided in 4.1. Statistics in table 5/6/21 of appendix. Datasets partially described in appendix D. Some dataset files available in implementation. Others download automatically through code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors refer in the appendix to the code for HPs. The values will have to be extracted from the code (no structured overview). There are some statements regarding HP tuning but this is not fully clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

Authors measure accuracy over random t/v/t splits and refer to a previous work for the procedure. Agg/var not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
