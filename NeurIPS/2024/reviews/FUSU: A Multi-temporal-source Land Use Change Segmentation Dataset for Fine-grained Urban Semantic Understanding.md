
## FUSU: A Multi-temporal-source Land Use Change Segmentation Dataset for Fine-grained Urban Semantic Understanding
Shuai Yuan, Guancong Lin, Lixian Zhang, Runmin Dong, Jinxiao Zhang, Shuang Chen, Juepeng Zheng, Jie Wang, Haohuan Fu
Keywords: 
NeurIPS/2024/Proceedings/97699 - FUSU: A Multi-temporal-source Land Use Change Segmentation Dataset for Fine-grained Urban Semantic Understanding.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state a link for their implementation in the abstract (https://github.com/yuanshuai0914/FUSU). In the readme they state download links for data, describe the datasets, some more cryptic descriptions and an acknowledge work they found interesting. The code has few comments and the repo is rather large without index. The architecture is given in figure 5. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide download links and a description for FUSU in the implementation. In table 1 they survey other datasets and give statistics on their own. The dataset construction is described in detail in sec 3. with examples and property description in table 2. Extensive statistics in figure 4. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

HP values are described in A.5.2. Acquisition is not specified. Config files can be found in the implementation but not clear which is for which experiment. No structured overview can thus be found on the HPs.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use IoU, mIoU per class as metrics. The results are single runs. The data set split in A.5.1. refers to the dataset link and is summarised in table 11, suggesting the authors give a static split in their presented dataset. Results are presented as either intra or inter dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise on image segmantation and land image data sets.
