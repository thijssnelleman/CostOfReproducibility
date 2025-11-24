## RASL- Robust alignment by sparse and low-rank decomposition for linearly correlated images
Yigang Peng, Arvind Ganesh, John Wright, Wenli Xu, Yi Ma
Keywords: Batch Image Alignment, Low-rank Matrix, Sparse Errors, Robust Principal Component Analysis, Occlusion, Corruption
extra_reviews/2011/Proceedings/RASL- Robust alignment by sparse and low-rank decomposition for linearly correlated images.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors state in the introduction a Matlab implementation of their method is available on their website (http://perception.csl.uiuc.edu/matrix-rank/rasl.html). This website however can not be found. However, after some debugging we found the corrected link (https://people.eecs.berkeley.edu/~yima/matrix-rank/Files/RASL_Code.zip). The readme explains how the code can be run for each figure in the paper, an index of the files and contact info. The code has some comments. There are no installation instructions or requirements documented. Implementation details provided in Sec 3.E. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors include five datasets in their implementation. They are described with great detail and citations in section IV.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide parameter values for their implementation in Sec 3.E and sec 4. Algorithm summarised in algorithm 1 and 2, with parameters. Values also found in the implementation per dataset as a structured overview found in the code but it is hard coded.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors conduct single runs per dataset and average per image in the dataset. Split not applicable. Most results are qualitative, but they also measure translation distance over percentage of occluded pixels. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
