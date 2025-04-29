
## Explore Internal and External Similarity for Single Image Deraining with Graph Neural Networks
Cong Wang, Wei Wang, Chengjin Yu, Jie Mu
Keywords: Computer Vision: CV: Applications, Computer Vision: CV: Computational photography
IJCAI/2024/Proceedings/0152 - Explore Internal and External Similarity for Single Image Deraining with Graph Neural Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/supersupercong/MSGNN). In their readme they provide a summarised version of their paper (excerpts/paragraphs) with visualisation and results. The state installation instructions, links to the data set downloads, links to visual results, how to train and evaluate the model and how to visualise the results. The code has very few comments, the settings are hardcoded into one of the scripts. In general the code could be a bit better documented and clean, but it serves as a good starting point.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors provide direct download links for five synthetic data sets in their implementation documentation. In section 4.1 they provide citations on the synthetic datasets and detail how they were used, and a short description + citation on the real world data set. In general these descriptions are a bit lacking and do not have any statistical information, thus some effort is needed to extract this from the citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state architecture details and hyperparameter values regarding the training procedure in 4.2. These values can easily be checked against the implementation docs regarding their completeness. No details are given on how these values were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The authors state how the data sets are used briefly in 4.1, where it is suggested that each data set has its own (static) predefined train/test split, but not explicitly stated except for Rain12. The metrics are not explained nor are citations provided for an explanation. The results indicate single runs. A lot is left to determine/verify for the independent investigators.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires an understanding of the task (image deraining) to understand the experiments conducted and the metrics used. The implementation documentation and the paper provide good examples which make the work more accessible.
