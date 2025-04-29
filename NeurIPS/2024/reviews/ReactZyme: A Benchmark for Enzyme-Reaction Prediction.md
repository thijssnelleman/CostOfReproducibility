
## ReactZyme: A Benchmark for Enzyme-Reaction Prediction
Chenqing Hua, Bozitao Zhong, Sitao Luan, Liang Hong, Guy Wolf, Doina Precup, Shuangjia Zheng
Keywords: 
NeurIPS/2024/Proceedings/97442 - ReactZyme: A Benchmark for Enzyme-Reaction Prediction.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/WillHua127/ReactZyme). In the readme the authors state the datasets with download links, index on the code files and functions, how to run the training. There are no installation instructions. There are readmes with links per data set directory. The code can use more comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors create their own dataset in the paper. They source it from two public datasets, state various details on the including statistics in table 1 and where they were sourced from. A direct download link to the data is given in the paper. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

The authors benchmark their method from figure 2 on the new dataset. However considered HPs are not clearly described. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors split the training data 10% randomly for validation. They split the data for train test on three types. The metrics are top-n, mean rank and MRR and explained in 5.1. The results are presented as averages but are seemingly single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expetise on enzyme (biomedical) tasks and data and geometrical deep learning.
