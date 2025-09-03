## How to Inject Backdoors with Better Consistency: Logit Anchoring on Clean Data
Zhiyuan Zhang, Lingjuan Lyu, Weiqiang Wang, Lichao Sun, Xu Sun
Keywords: 
ICLR/2022/Proceedings/6256 - How to Inject Backdoors with Better Consistency: Logit Anchoring on Clean Data.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. Although their study is mainly a theoretical analysis, it will still be required to re-implement the code to reach the same conclusions.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors use CIFAR-10 and Tiny-ImageNet for CV, IMDB and SST-2 for NLP. All have citations provided. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors present the results with an ablation study of the parameter delta in table 2. The details on how the hyperparameters were set for the models are given in appendix B.2.1. and B2.2. although a structured overview is missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure ASR, Top-1/5 Accuracy, ASR+ACC and five instance-wise consistency metrics. Most are standard/straightforward, and details are given in 2.3. Results are single run. The authors conduct backdoor training, for which they provide details in the appendix.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
