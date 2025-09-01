## Comparing Distributions by Measuring Differences that Affect Decision Making
Shengjia Zhao, Abhishek Sinha, Yutong He, Aidan Perreault, Jiaming Song, Stefano Ermon
Keywords: 
Award: Outstanding Paper Award
ICLR/2022/Proceedings/1006 - Comparing Distributions by Measuring Differences that Affect Decision Making.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their code in footnote 1 on page 6 (https://github.com/a7b23/H-Divergence). In the readme they state instructions how to run the experiments. No installation instructions provided in the readme, although some details in the comments of the files. The code has a nice amount of comments. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors provide download links for HIGGS and MNIST in the implementation link. Blob and HDGM are generated and code is given. Citations provided for all. Details/overviews are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

The authors state they tune the hyper-parameters on the training set in 4.2. How this is done is unclear. The values are recorded in the python scripts of the implementation but a structured overview is not given.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors split the dataset into two parts for training and validation, but it is not clear how this is done. The authors measure average test power and present it with one standard error over N samples with 10 repitions. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
