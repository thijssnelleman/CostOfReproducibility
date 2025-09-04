## Planckian Jitter: countering the color-crippling effects of color jitter on self-supervised training
Simone Zini, Alex Gomez-Villa, Marco Buzzelli, Bartłomiej Twardowski, Andrew Bagdanov, Joost van de Weijer
Keywords: 
ICLR/2023/Proceedings/11852 - Planckian Jitter: countering the color-crippling effects of color jitter on self-supervised training.pdf
Project URL: https://openreview.net/attachment?id=Pia70sP2Oi1&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/TheZino/PlanckianJitter). In the readme the authors state the installation requirements, that they published their method in a library, examples how to use the code. The code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors use CIFAR-100, ImageNet, Flowers-102, VegFru, CUB-200, T1K+, and USED. Citations provided for most. Details on datasets are scarce. No links provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors state parameter values in text of 4.1. Structured overview is missing. Values are taken from previous works (cited) with slight modifications to the architecture for the task. They construct six different pipeline configurations for analysis.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors measure accuracy, use other datasets for evaluations as split and present single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
