
## CoLLIE: Continual Learning of Language Grounding from Language-Image Embeddings
Gabriel Skantze, Bram Willemsen
Keywords: 
JAIR/2022/Proceedings/13689 - CoLLIE: Continual Learning of Language Grounding from Language-Image Embeddings.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the reproducibility statement (https://github.com/gabriel-skantze/CoLLIE). In the readme they state installation notes and how to download the LAD dataset, and how to run two different experiments including result visualisation. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use the LAD dataset (Cited, link in implementation) which they describe briefly in section 3, and also the KTH Tangrams dataset (cited, included in the implementation).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The architecture of the models can be found in the code, although it is a bit 'tricky' to read (no config files etc). There are also some hyperparameters stated throughout the text. Its not clear how the values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure Mean Reciprocal Rank (MRR) averaged over 50 iterations. The authors perform zero-shot performance, the authors state the data split in 5.1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on NLP/CV and continual learning.
