
## STDiff: Spatio-Temporal Diffusion for Continuous Stochastic Video Prediction
Xi Ye, Guillaume-Alexandre Bilodeau
Keywords: CV: Computational Photography, Image & Video Synthesis, ML: Deep Generative Models & Autoencoders, CV: Representation Learning for Vision, ML: Deep Learning Algorithms
AAAI/2024/Proceedings/28952 - STDiff: Spatio-Temporal Diffusion for Continuous Stochastic Video Prediction.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/XiYe20/STDiffProject). There they provide examples and a diagram of their method, installation instructions including installing dependencies, links to download two of the data sets, a general directory layout required for the data and instructions for training and testing. The code has a descent amount of comments and is quite well organised. The authors also provide configuration yaml files. Data loaders are also present, as well as metric calculations. The paper provides more graphical representations of the method/process, including architecture schematics, pseudo code and examples.


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors use 5 different data sets for which they provide citations. Download links for two are available on the GitHub, for the others the authors refer the reader to the original website without link. No statistics on the data sets are provided. Data set configs can be found in the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide configuration files in the implementation documentation which has configurations for the data set but for each method as well. It is thus very easy to look up the configuration used. The authors refer to previous works for determing the pas and future frames settings. There are no details on how these values were acquired, suggesting human optimisation, but no budget is specified for this.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Full details for each experiment are given per data set, but there is no explanation on the meaning of the metrics, thus raising the effort required. However the authors do provide code on this in their implementation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method deals with spatio temporal vision data, requiring a good understanding on both due to the complexity of the method and the intersection of many different domains. This is not for a lack of trying by the authors as they provide a comprehensive introduction on the topics.
