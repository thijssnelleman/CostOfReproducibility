
## C-Face: Using Compare Face on Face Hallucination for Low-Resolution Face Recognition
Feng Han, Xudong Wang, Furao Shen, Jian Zhao
Keywords: 
JAIR/2022/Proceedings/13816 - C-Face: Using Compare Face on Face Hallucination for Low-Resolution Face Recognition.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state 4.2. their method was implemented in PyTorch. Pseudocode in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use the CASIA-WebFace dataset, LFW dataset and CelebA dataset and provide citations on all. No other information.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state the hyperparameters of algorithm 1 per equation in 4.2, as well as more default HPs. Acquisition not specified. Overview not given, neither on what they consider the hyperparameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use one dataset for training the other for testing. The authors measure PSNR and SSIM which are named but not explained in 4.1. and verification rate for table 1/4 which is stated in 4.3.2. Results are single runs, except in 4.4 where they conduct 10-fold cross validation but don't state aggregation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on CV and face tasks.
