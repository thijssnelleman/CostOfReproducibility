## Context Aware Saliency Detection
Stas Goferman, Lihi Zelnik-Manor, Ayellet Tal
Keywords: Image saliency, visual saliency, context aware
extra_reviews/2011/Proceedings/Context Aware Saliency Detection.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors do not provide a link to their implementation. An overview of the method is given in figure 1/2/3. There are some notes on how their method was implemented in section 3, but they do not mention specifics such as packages or frameworks.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use the datasets of X. Hou and L. Zhang. Saliency detection: A spectral residual approach and provide a citation, a short description. Statistics less applicable in this case. No direct link given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors describe the method in the formulae in section 3. Here they state the value of parameter c = 3, and the scale parameter R, which they vary over a grid. They also state a threshold level Si > 0.8. No overview given, only present in text. It is not clear how each value was acquired, although one is varied over a grid for the experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure AUC on the dataset. Split is not applicable. Results are single run. Other results are qualitative. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
