## LightHGNN: Distilling Hypergraph Neural Networks into MLPs for 100x Faster Inference
Yifan Feng, Yihe Luo, Shihui Ying, Yue Gao
Keywords: 
ICLR/2024/Proceedings/17940 - LightHGNN: Distilling Hypergraph Neural Networks into MLPs for 100x Faster Inference.pdf
Project URL: https://openreview.net/attachment?id=lHasEfGsXL&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

Pseudo code in appendix A, algorithm 1. No implementation given.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

News20, CA-Cora, CC-Cora, CC-Citeseer, DBLP-Paper, DBLP-Term, DBLP-Conf, IMDB-AW. All cited. Details + statistics in appendix C. No links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

HP values summarised in appendix E table S5/S6. HP sensitivty of 2 parameters analysed in 5.5. not all values motivated.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

We run 5 times with different random seeds for each experiment and report the average score and standard deviation. Data split in appendix E. Authors measure accurracy, memory (mb) and runtime (s).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
