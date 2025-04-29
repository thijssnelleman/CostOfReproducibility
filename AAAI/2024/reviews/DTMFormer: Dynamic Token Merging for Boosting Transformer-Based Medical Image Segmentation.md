
## DTMFormer: Dynamic Token Merging for Boosting Transformer-Based Medical Image Segmentation
Zhehao Wang, Xian Lin, Nannan Wu, Li Yu, Kwang-Ting Cheng, Zengqiang Yan
Keywords: CV: Medical and Biological Imaging, CV: Segmentation
AAAI/2024/Proceedings/28770 - DTMFormer: Dynamic Token Merging for Boosting Transformer-Based Medical Image Segmentation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their github repository (https://github.com/iam-nacl/DTMFormer). They have clear instricutions on what is required to run the code and how to do so, including links to three data sets. Their code has a sufficient amount of comments to make it easily understandable, and the layout of the repository is easy to follow. The two code files however can be parametrised and instructions on this would also help, however when running with --help there are help comments available.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors present three datasets in their work that are publicly available, provide citations on them, give a full description on them, and link where they can be acquired in their implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The algorithm configuration has default values documented in the implementation documentation. The authors provide the values of a few hyperparameters per data set in their method. It is unclear however how these values were acquired and under what budget.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors clearly state and motivate their evaluation metrics, state the division of training/testing split, but the authors do not specify how the results are to be produced. They seem to indicate a one-shot result in their tables.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The authors provide a comprehensive documentation on their method, with many examples. However, the method is domain specific to medicine and computer vision, and applies transformers to this domain. Thus a certain amount of expertise in each of these three domains would be recommended.
