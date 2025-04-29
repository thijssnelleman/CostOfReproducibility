
## Semantic Diffusion Network for Semantic Segmentation
Haoru Tan, Sitong Wu, Jimin Pi
Keywords: 
NeurIPS/2022/Proceedings/55257 - Semantic Diffusion Network for Semantic Segmentation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state the framework they use with citation in 5.1. They state in the checklist [YES] on the question if code as included, but this cannot be found. Overview on the method in figure 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use ADE20K and Cityscapes benchmark datasets. Citations and brief descriptions are provided. The statistics are very high level. No links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

HP values are informally stated in 5.1 (No structured overview). They state these values were selected from other works for fair comparison.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Datasplits are stated in sec 5.1. metrics are mIoU. In the table caption they state the results are on the validation set. They link in 5.2. for the results on the test set of city scapes. Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on semantic segmentation.
