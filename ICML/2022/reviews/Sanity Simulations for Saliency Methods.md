
## Sanity Simulations for Saliency Methods
Joon Kim, Gregory Plumb, Ameet Talwalkar
Keywords: 
ICML/2022/Proceedings/16383 - Sanity Simulations for Saliency Methods.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/wnstlr/SMERF). In the readme they state installation requirements, extensive details on the datasets, how to run the experiments from the paper with an explanation of the parameters, how to plot the results, and a link to the exact outputs of the paper. The code has a decent amount of comments. An overview of the workflow is given in figure 5.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide instructions on how to regenerate the data sets in the implementation, and provide a direct link for another in the implementation.The authors explain the TextBox dataset in appendix A.1. which is a generated data set (generation process explained) and the code for it is available in the implementation. Their own method is also a synthetic data generator.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors method is a synthetic generation framework, so hyperparameters are not really applicable (HPs regarding data generation are handled in section Data). Nonetheless, the authors provide HP details on the trained model in section A.2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use IOU metrics and provide a citation/explanation, and a 'new' metric called AFL for which they provide a citation and description (more details in appendix A). The authors present the results over 'buckets' (method specific) with average aggregation and standard deviation. There is a mention regarding 'test accuracy' in B.9. but its not clarified otherwise regarding train/testing data.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on data simulation/generation.
