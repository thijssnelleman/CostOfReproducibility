## AutoTransfer: AutoML with Knowledge Transfer - An Application to Graph Neural Networks
Kaidi Cao, Jiaxuan You, Jiaju Liu, Jure Leskovec
Keywords: 
ICLR/2023/Proceedings/11462 - AutoTransfer: AutoML with Knowledge Transfer - An Application to Graph Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to the implementation in footnote 3 of the introduction (https://github.com/snap-stanford/AutoTransfer). The repository has installation instructions (requirements.txt, more details to a linked repo in readme), and a brief example for running the code. The structure is huge and needs an index. Comments seem to be good.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors use Coauthor-Physics, CoraFull and OGB-Arxiv, COX2, IMDB-M, and PROTEINS and provide citations for all. No links or other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors conduct an HPO study in their work which is well documented and configuration files are available per experiment in the implementation.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Data set splits detailed in 5.1. The authors report the average test accuracy and the standard deviation over ten runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
