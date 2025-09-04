## Learning Kernelized Contextual Bandits in a Distributed and Asynchronous Environment
Chuanhao Li, Huazheng Wang, Mengdi Wang, Hongning Wang
Keywords: 
ICLR/2023/Proceedings/11356 - Learning Kernelized Contextual Bandits in a Distributed and Asynchronous Environment.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors do not provide their implementation. Overview in figure 1, detailed pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors use a synthetic dataset, which they describe in 5.1 but do not share the implementation, UCI Datasets MagicTelescope and Mushroom, MovieLens and Yelp. All have descriptions and citations but no direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors state they conduct a grid search for a part of the parameters in section 5. Structured overview missing. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[5]

The authors report communication and regret on the datasets, splits not stated. Metrics not clarified, although regret is pretty standard. Aggregation and variation of plot not clarified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
