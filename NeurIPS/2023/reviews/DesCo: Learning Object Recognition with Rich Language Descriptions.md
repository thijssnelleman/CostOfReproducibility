
## DesCo: Learning Object Recognition with Rich Language Descriptions
Liunian Li, Zi-Yi Dou, Nanyun Peng, Kai-Wei Chang
Keywords: 
NeurIPS/2023/Proceedings/72079 - DesCo: Learning Object Recognition with Rich Language Descriptions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors publish their implementation online (https://github.com/liunian-harold-li/DesCo). In the readme they state installation details, links to pretrained models and their configurations, a quick starts example, pretraining examples, and how to evaluate several benchmarks with parameter explanations and some notes on the code. The repository is huge and needs an index. The code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

In the implementation there is a separate data readme with a downloda link to the COCO dataset (and LVIS), Objects365, Flickr30K and MixedGrounding. Not found for Omnilabel. Citations and brief descriptions given in 4.2. Statistics too shallow.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The hyperparameters per experiment (phase) are given in the implementation config files and briefly described in the implementation details of 4.2. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Data set splits are given in the implementation config files. Results are single model. Metrics are not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on CV (Object recognition) and NLP
