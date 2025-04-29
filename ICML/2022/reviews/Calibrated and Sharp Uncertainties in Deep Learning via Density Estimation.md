
## Calibrated and Sharp Uncertainties in Deep Learning via Density Estimation
Volodymyr Kuleshov, Shachi Deshpande
Keywords: 
ICML/2022/Proceedings/17391 - Calibrated and Sharp Uncertainties in Deep Learning via Density Estimation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. Pseudo code is available in algorithm 1 2 and 3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(11/11)

The authors use three public image classification benchmarks. Furthermore they use 8 regression benchmarks of UCI. No citations provided, statistics are shallow. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors describe the models in 6.1 with architectures and several HP values. Some are seemingly missing. The parameters from the pseudo code do sime given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate Maen Average Error and Check score for table 2 and accuracy/calibration for table 3. Table 3 is single runs on the test set. Table 2 has randomly 25% data reserved for testing in each run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on calibration in deep learning
