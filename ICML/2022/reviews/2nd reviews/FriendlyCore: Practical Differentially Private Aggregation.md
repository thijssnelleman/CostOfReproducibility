## FriendlyCore: Practical Differentially Private Aggregation
Eliad Tsfadia, Edith Cohen, Haim Kaplan, Yishay Mansour, Uri Stemmer
Keywords: 
ICML/2022/Proceedings/16323 - FriendlyCore: Practical Differentially Private Aggregation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

Implementation is not included +4. Implementation description limited to mentioning Python +3. Pseudocode is included with sufficient detail, architecture figures n/a. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

Synthetic data experiments: Simulation code was linked. Task is well described. Simulation parameters specified. Real-world dataset: No direct link, but citation included +1. Description and statistics included. Dataset is public. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters were explained in text, but no summary +1. Hyperparameter values are described well. Acquisition strategy and budget are not explicitly mentioned +2. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Some metrics were not included, though those results seemed qualitative (clustering results). L2-error needs no elaboration, "normalized k-Means loss" was explained. Data splits not applicable (unsupervised tasks). Strategy and details explained in main text, further expanded on in appendix. Aggregation was done visually, visualisation not explained explicitly +1. Measure of distribution not explicitly explained +1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8] 

The paper is quite theoretical, requiring more expert knowledge and considerable to interpret the supplied mathematics, especially because part of the information was contained in the appendix. On the other hand, much of the mathematics included were fundamental, requiring general theoretical knowledge, but not expert knowledge specific to the averaging and clustering tasks used to evaluate.
