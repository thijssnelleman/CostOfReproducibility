
## Locally Hierarchical Auto-Regressive Modeling for Image Generation
Tackgeun You, Saehoon Kim, Chiheon Kim, Doyup Lee, Bohyung Han
Keywords: 
NeurIPS/2022/Proceedings/53827 - Locally Hierarchical Auto-Regressive Modeling for Image Generation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors state frameworks an libraries (with versions) used for their implementation in appendix A.3. including direct links for three implementations used for 'major routines'. Overview given in figure 2 and 3. Implementation not given

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use ImageNet, Conceptual Caption and Conceptual-12M. Citations given, but no other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors report the hyperparameters in appendix A and table A. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use the train split of ImageNet and present results on ImageNet validation, CC3M validation (all static splits). Metrics are FID, CLIP (citation given, not defined) and precision and recall (standard) as well. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on auto-regressive modelling and CV (image generation).
