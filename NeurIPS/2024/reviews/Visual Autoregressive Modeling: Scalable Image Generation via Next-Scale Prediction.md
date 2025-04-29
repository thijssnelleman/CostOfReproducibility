
## Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction
Keyu Tian, Yi Jiang, Zehuan Yuan, BINGYUE PENG, Liwei Wang
Keywords: 
Award: Best Paper
NeurIPS/2024/Proceedings/1181 - Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction.pdf
Project URL: https://var.vision

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/FoundationVision/VAR). In the readme they state news, links to demo website and notebooks, show the results, a zoo fo their models with details, how to install, links to the dataset and where to place it, how to run the training scripts, how to infer, list of third party usage with direct links. The code has an okay amount of comments (more would be welcome but no deduction). Structure is overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors provide a direct link to the data set in the implementation (ImageNet). No details given on the dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors evaluate their method with various architectures. Other parameter values are directly linked to this depth throug a formula or set to a fixed values. No acquisition specified for the latter parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use FID (acronym explained in abstract), inception score, precision and recall (latter three standard). The authors specify in table 1 a row about validation data, and this set is mentioned in sec 5.2. Real spit is not specified. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on CV regarding image generation. 
