## BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion
Fu-Yun Wang, Da-Wei Zhou, Liu Liu, Han-Jia Ye, Yatao Bian, De-Chuan Zhan, Peilin Zhao
Keywords: 
ICLR/2023/Proceedings/11713 - BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/G-U-N/ICLR23-BEEF). They list which packages are needed to run the scripts (without versions however), how to run the scripts with examples, and results. The code is generally missing comments. The repository could use more info on how to use and the structure.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use CIFAR-100, ImageNet100/1000, provide citations and descriptions. The datasets download automatically in the code. Statistics lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors provide json config files for the datasets in the implementation. The authors conduct an analysis on sensitive parameters in section 4.3.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use the standard data splits of the datasets. They report average and last accuracy of single runs on the test set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
