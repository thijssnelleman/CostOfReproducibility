## Source-Free Adaptation to Measurement Shift via Bottom-Up Feature Restoration
Cian Eastwood, Ian Mason, Chris Williams, Bernhard Schoelkopf
Keywords: 
ICLR/2022/Proceedings/6285 - Source-Free Adaptation to Measurement Shift via Bottom-Up Feature Restoration.pdf
Project URL: https://openreview.net/attachment?id=1JDiK_TbV4S&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in section 5.1 (https://github.com/cianeastwood/bufr). In the readme they state installation requirements, Datasets and their download links and where it should be placed to use the code, how to run the code, how to configure the code, where results can be found and how to analyse, and a list of results. Code has good comments, structure is overseeable.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors provide download links for all datasets in the readme of the implementation. The authors discuss the datasets at length in appendix F with citations and visualisations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors state architecture details in 5.1. and provide hp values in appendix G and that some HP values were searched over grids. Structured parameter values can be found in the implementation. Not all value acquisition is clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors present the results with mean and std dev over Accuracy and expected calibration error (ECE, citation provided and briefly explained), over five random runs. The authors state a 80-10-10 t/v/t split in 5.1. at random and report results on the test set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
