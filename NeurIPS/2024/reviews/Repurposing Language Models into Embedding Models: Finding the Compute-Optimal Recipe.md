
## Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe
Albert Q. Jiang, Alicja Ziarko, Bartosz Piotrowski, Wenda Li, Mateja Jamnik, Piotr Miłoś
Keywords: 
NeurIPS/2024/Proceedings/93887 - Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their implementation online (https://github.com/SeqDM/Efficient-Embeddings). In the readme the authors state installation instructions, how to download and preprocess the data and how to run training + evaluation and where the results will be stored. The code has an okay amount of comments, but the structure is quite large so an index would very much be welcome. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors state the fine-tune dataset BAAI BGE in 4.1 with citation and a downstream evaluation dataset MTEB with citation and a description on it in appendix B. In appendix I they provide a direct link to the BAAI BGE dataset. There is no clear direct link for mteb but the subset extraction code is available in the implementation. Statistics not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state hyperparameter fine-tuning in 4.2. and hyperparameter values in 4.1 and a full list in appendix E. In E.1. they empirically select the learning rate, in E.2. they conduct a grid search for the temperature and weight decay, in E.3. they describe the pooling type selection. The authors give the values per experiment.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The experimental setup is given in 4.1. Here they state how they divide the computational budget, on what data sets is being trained (fine tuned) and tested. The metrics are loss and number of parameters in the model. There is a note on train and test split in appendix F. Most of the results are fine tuning results (training dataset). But this note in appendix F does make it a bit unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on LLMs and NLP in general.
