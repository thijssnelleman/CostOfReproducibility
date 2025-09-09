## Let Models Speak Ciphers: Multiagent Debate through Embeddings
Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu Chen, Tianyi Liu, Jianbo Yuan, Bryan Plummer, Zhaoran Wang, Hongxia Yang
Keywords: 
ICLR/2024/Proceedings/17640 - Let Models Speak Ciphers: Multiagent Debate through Embeddings.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

No implementation given. Pseudo code in algorithm 1. Overview in fig 1-2.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(2/3)

GSM8K, MMLU, and "mathematical expressions comprising six unique two-digit numbers that include addition, multiplication, and subtraction operations" (Not provided). Datasets have brief descriptions and all have a citations provided. No links or statistics, and the math problem dataset (or its generator) is not given, albeit a simple problem and should be accesible to recreate.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

Parameters given in algorithm 1, varied values of R/n per experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Authors measure accuracy over different rounds (responses with temperature e.g. seed), test set detailed in 4.1. Variation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
