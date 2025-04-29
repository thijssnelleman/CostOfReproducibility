
## Beyond neural scaling laws: beating power law scaling via data pruning
Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari Morcos
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/1948 - Beyond neural scaling laws: beating power law scaling via data pruning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the supplementary materials (https://colab.research.google.com/drive/1in35C6jh7y_ynwuWLBmGOWAgmUgpl8dF?usp=sharing). The notebook can use more text documentation. Since its on Google Colab, installation is handled automatically.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/3)

The authors use ImageNet, CIFAR-10 and SVHN datasets. No citations, links, statistics or descriptions on the data itself. In appendix B they do detail how the data was treated. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Hyperparameter values stated in appendix B. No structured overview or acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Results are averaged over 10/100 independent draws. Metrics are top-k validation accuracy. The data set the authors present the results on are stated per figure. Data split and variation specified in appendix B. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on data pruning.
