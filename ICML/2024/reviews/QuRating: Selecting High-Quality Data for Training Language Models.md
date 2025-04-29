
## QuRating: Selecting High-Quality Data for Training Language Models
Alexander Wettig, Aatmik Gupta, Saumya Malik, Danqi Chen
Keywords: 
ICML/2024/Proceedings/34502 - QuRating: Selecting High-Quality Data for Training Language Models.pdf
Project URL: https://github.com/princeton-nlp/QuRating

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share their implementation online (https://github.com/princeton-nlp/QuRating). In the readme the authors state details on where to find datasets/models with direct links, installation instructions, how to run the code, how to annotate data, how to select data and training instructions. Some of the files in the code are well commented but some could do better. The repository structure is large but overseeable with all the examples in the readme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(11/11)

The authors provide links to datasets in the implementation. They also include a link in the paper. The first dataset the authors discus is their own (publicly released) dataset. They discuss how this dataset was acquired in detail. This dataset is used for training. The authors also evaluate these trained models on 10 benchmark datasets on which all they provide citations. Not many other details are given on these datasets except brief task descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the hyperparameter selection in Appendix B.2 (grid search with grids specified). The full used parameters are summarised in appendix D. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state how the training set was selected and the validation set. All other datasets are used for evaluation. The authors do not explain the used metrics. Results are over a single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in LLMs.
