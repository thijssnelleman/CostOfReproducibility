
## VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks
Yang Li, Shaobo Han, Jonathan Shihao Ji
Keywords: 
NeurIPS/2024/Proceedings/93861 - VB-LoRA: Extreme Parameter Efficient Fine-Tuning with Vector Banks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors link their implementation in the abstract (https://github.com/leo-yangli/VB-LoRA) and state their method has been published in a software package which they link. In the readme they introduce the method, provide instructions on how to install and reproduce the results from the paper in detail. Only one file seems to really contain the authors method, although some other files can be identified as adapted by the authors. The code has decent comments, but an overview on the structure is needed to understand what was made by the authors. Figure 2 gives an overview. Pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

In 4.1 the authors state they used the GLUE benchmark (with direct link and citation), and state the tasks they focus on from the benchmark. In 4.2. the authors state they use the E2E dtaset (citation + link). In 4.3. they use the Cleaned AlpacaDataset (link and citation) and MT-BENCH (same). In 4.4 they use MetaMathQA (Link and citation) for training and GSMK8K (same) for testing. No statistics or lengthy descriptions given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are discussed in A.1. Here they provide in a tabular format the parameters per method per dataset/experiment. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors report median performance over 5 random runs in table 1, mean over 3 random seeds in table 2, and single model runs in table 3 and 4. The metrics are defined in the caption of table 1 (all standard), in table 2 number of parameters but the performance is not explained, in table 3 and 4 the same (score is not explained). The test set is explained for 4.2, in 4.3 mt bench is evaluation set, and 4.4 GSM8K. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on NLP, model pruning and fine tuning.
