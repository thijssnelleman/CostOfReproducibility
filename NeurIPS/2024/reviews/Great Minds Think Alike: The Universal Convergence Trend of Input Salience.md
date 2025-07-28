
## Great Minds Think Alike: The Universal Convergence Trend of Input Salience
Yipei Wang, Jeffrey Siskind, Xiaoqian Wang
Keywords: 
NeurIPS/2024/Proceedings/96455 - Great Minds Think Alike: The Universal Convergence Trend of Input Salience.pdf
Project URL: https://openreview.net/attachment?id=7PORYhql4V&name=supplementary_material

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

There is no link in the paper regarding the implementation but there is a supplementary material link on the openreview link of the publication page on neurips (https://openreview.net/attachment?id=7PORYhql4V&name=supplementary_material). The code has nearly no comments. In the readme the authors state installation requirements, tutorials regarding training and visualisation of the experiments. The implementation is very small and easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The code has automatic downloaders for CIFAR10, CIFAR100. There are citations on these datasets in section 3. TinyImagenet is cited as well in sec 3 but no downloader or link given. No descriptions or statistics given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values are stated in sec 3. Model details regarding architectures are stated in table 2 and appendix B. There are parameters defined in the code arguments with default values, which overlap with those given in the code. The K-value is varied over the experiments. The acquisition of most parameters is not defined.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evalaute similarity metric (cosine similarity) over width k. They also produce heatmaps. Metrics are describe in sec 3.1. In sec 2.1. its stated experiments are conducted on the test sets, but these are not given for the data sets. However from the code its clear they use static test sets provided by the source. Results are per model k (no repition)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on DNNs and input salience.
