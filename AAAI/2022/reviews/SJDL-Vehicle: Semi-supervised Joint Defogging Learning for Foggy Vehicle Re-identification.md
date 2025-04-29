
## SJDL-Vehicle: Semi-supervised Joint Defogging Learning for Foggy Vehicle Re-identification
Wei-Ting Chen, I-Hsiang Chen, Chih-Yuan Yeh, Hao-Hsiang Yang, Jian-Jiun Ding, Sy-Yen Kuo
Keywords: Computer Vision (CV)
AAAI/2022/Proceedings/19911 - SJDL-Vehicle: Semi-supervised Joint Defogging Learning for Foggy Vehicle Re-identification.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/AaronCIH/SJDL-Foggy-Vehicle-Re-Identification--AAAI2022). In the readme they give details on the method, updates on the implementation, network architecture schematics, data examples, results, how to set up an environment for their implementation, how to do the data preparation, training instructions, a short common problems (sort of 'FaQ'), pretrained models link and instructions on how to run the test. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use two benchmark data sets and combine it into one, selecting samples that fit their problem/task. They present some statistics on the dataset and examples. They also construct a synthetic data set and provide details on how this is done. However their implementation documentation suggests that (part of) their data is not public. This would have to be investigated

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state many hyperparmaeter values in their paper and learning schemes are also provided. The implementation docs has a very accesible documentation on their values as well. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state and cite a previous work for their evaluation method. The metrics are stated, one of which is very common but the other could use an explanation. More details could have been given, however with the implementation docs provided this should not be too much effort to extract.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a very good understanding of semi-supervised learning, and computer vision. This is not due to a lack of trying by the authors, rather it is a very complex topic and the authors deal with many constraints such as lack of data which they have to solve by synthesis.
