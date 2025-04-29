
## Natural image synthesis for the retina with variational information bottleneck representation
Babak Rahmani, Demetri Psaltis, Christophe Moser
Keywords: 
NeurIPS/2022/Proceedings/53921 - Natural image synthesis for the retina with variational information bottleneck representation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

Overview given in figure 1. Implementation link provided in appendix section 9 (https://github.com/Babak70/Natural_image_synthesis). In the readme they state installation requirements, how to run the code with various examples, how to set parameters. Code has okay comments. Structure is a bit vague and code can use a cleanup.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors discuss datasets in 5.1 and 5.2. They are briefly described and cited. A few more details are given in the appendix. No statistics or direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors evaluate the method over various HP values Beta. More HP values are stated in appendix 2. Structured overview missing. Acquisition not specified for others (only beta is grid evaluated).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the metrics in sec 5.2. Data split is given in 5.2. The authors report results over three folds. Aggregation / variation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on image synthesis and information bottlenecks.
