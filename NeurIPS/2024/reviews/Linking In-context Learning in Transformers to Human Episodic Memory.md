
## Linking In-context Learning in Transformers to Human Episodic Memory
Ji-An Li, Corey Zhou, Marcus Benna, Marcelo G Mattar
Keywords: 
NeurIPS/2024/Proceedings/96248 - Linking In-context Learning in Transformers to Human Episodic Memory.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/corxyz/icl-cmr). In the readme they state the method installation requirements, a quick start with a link to a demo notebook and what they show inthere, how to replicate the experiments with detailed code instructions, the pretrained models used with a link. The code has a good amount of comments. Although the repository is not small, most directory structures are directly regarding the output of their experiments, and only src contains code which is overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use Google's C4 dataset (citation), PEERS data set (citation) but not much other details are given regarding the datasets used. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The models used are pretrained but there is a note on model fitting in the appendix and figure 7. No parameters given/described. There are some values that can be extracted from the code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The metrics are explained in detail with citations in sec 5. and appendix E. The authors use standard error as variance but aggregation is not given. Repetition is not explained. The results are on training/trained models, no data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on transformers, induction heads specifically and CMR.
