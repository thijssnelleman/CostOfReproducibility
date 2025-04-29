
## Point Transformer V2: Grouped Vector Attention and Partition-based Pooling
Xiaoyang Wu, Yixing Lao, Li Jiang, Xihui Liu, Hengshuang Zhao
Keywords: 
NeurIPS/2022/Proceedings/53692 - Point Transformer V2: Grouped Vector Attention and Partition-based Pooling.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/Pointcept/PointTransformerV2). In the readme they give an overview on the method, post news, give an overview on the readme, installation instructions, data prep steps, quick start with various examples, how to test the model, a detailed model zoo with various scripts and download links for logs, configs etc. and ackownledgements for other implementations they build upon. Code needs more comments. Structure is quite large and can use index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors provide a link to ScanNet v2, S3DIS and Semantic KITTI datasets in the implementation. The authors use ScanNet and S3DIS in their experiments and provide citations on them. No statistics or descriptions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Hyperparameter values are summarised per dataset in appendix A. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Data split and metrics given in 4.1. Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on transformers.
