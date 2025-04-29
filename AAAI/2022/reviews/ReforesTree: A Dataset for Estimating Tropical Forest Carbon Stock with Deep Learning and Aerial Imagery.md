
## ReforesTree: A Dataset for Estimating Tropical Forest Carbon Stock with Deep Learning and Aerial Imagery
Gyri Reiersen, David Dao, Björn Lütjens, Konstantin Klemmer, Kenza Amara, Attila Steinegger, Ce Zhang, Xiaoxiang Zhu
Keywords: AI For Social Impact (AISI Track Papers Only)
AAAI/2022/Proceedings/21471 - ReforesTree: A Dataset for Estimating Tropical Forest Carbon Stock with Deep Learning and Aerial Imagery.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors introduce a new data set in their paper. They demonstrate a baseline CNN on it, but do not provide a link to their implementation. They state they use a pretrained model (cited) and fine tune it, which metric is optimised, and how the data was fit to feed into the pretrained model. Thus, although the implementation is absent, some key details are given on how it can be reproduced.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors present their own benchmark data set, publicly available. Many details on the data set are provided, such as statistics, key problems and scope. However no direct online link can be found to the data, so this is the only effort that will have to be made.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors use a pretrained model and fine tune it. However, some key hyperparameters are missing, which could supposedly be provided in the source paper of the pretrained model, but this would have to be determined as it is not stated in the paper.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state some details on the distributions between training and testing sets, but now how the division is done. This makes reconstructing the procedure not without effort. There is also little detail on the training procedure itself. There is a short definition on the metrics but no clear explanation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires some understanding of data analysis and statistics. Knowledge on the task is welcome but not required due to the clear and lengthy introduction of the topic by the authors.
