## Automatic Chain of Thought Prompting in Large Language Models
Zhuosheng Zhang, Aston Zhang, Mu Li, Alex Smola
Keywords: 
ICLR/2023/Proceedings/11360 - Automatic Chain of Thought Prompting in Large Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/amazon-science/auto-cot). In the readme they state installation requirements, where to download the datasets, a quick start notebook, how to run the code. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(10/10)

The authors provide two download links for datasets in their implementation. The authors use MultiArith, GSM8K, AddSub, AQUA-RAT, SignleEq, SVAMP, CSQA, StrategyQa, Laster Letter Concatenation, Coin Flip and provide citations for all. The links contains the files of all datasets. The tasks of the datasets are named in the appendix as well and an overview is given in table 9 of appendix B.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors use a live model (GPT-3) and state the parameters used in appendix B.2.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report mean and standard deviation and run the experiments with three random seeds, and measure accuracy. Results are specified on either training set or test set (static split).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
