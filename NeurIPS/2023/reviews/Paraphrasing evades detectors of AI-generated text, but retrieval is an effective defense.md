
## Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense
Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, Mohit Iyyer
Keywords: 
NeurIPS/2023/Proceedings/71402 - Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors place a link to their implementation in footnote 1 (https://github.com/martiansideofthemoon/ai-detection-paraphrases). In the readme they state updates, how to run their model and where to download it, how to verify everything works, how to reproduce the experiments from the paper in great details. There is a file for installation requirements. The repository structure is large and could use an index. More comments are needed.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors build a dataset in section 3. They state the process in details with a figure 2 as overview. Links to the dataset are given in the implementation. Detailed statistics are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

Hyperparameters remarks are made in a few footnotes of the paper, but a structured overview is not given. There are scripts in the implementation with parameter values, but these are relatively unstructured. For some values it is stated they are 'default'.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors describe the evaluation metrics in 4.1. with details and citations. The results are single model in table 1, figure 3 and 4. The authors state there is a test set split but not how this is done. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on NLP and text generation detection.
