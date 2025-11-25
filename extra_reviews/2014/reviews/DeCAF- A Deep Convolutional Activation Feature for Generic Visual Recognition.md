## DeCAF- A Deep Convolutional Activation Feature for Generic Visual Recognition
Jeff Donahue, Yangqing Jia⇤, Oriol Vinyals, Judy Hoffman, Ning Zhang, Eric Tzeng, Trevor Darrell
Keywords: 
extra_reviews/2014/Proceedings/DeCAF- A Deep Convolutional Activation Feature for Generic Visual Recognition.pdf
$PROJECT URL$

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 of section 3.1. (https://github.com/UCBAIR/decaf-release). They provide examples on how to use the code in decaf/demos, and an installation script, as well as details regarding errors you may experience. They also state the package is deprecated and a new version is available online elsewhere. The codebase is large and could use an index. Comments are available throughout the package and are quite detailed.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(7/7)

The authors use benchmark datasets; SUN-397, ILSVRC-2012, Berg et al. (2012) dataset, Caltech-101, Ofﬁce dataset, SURF dataset, Caltech-UCSD birds dataset. All are cited, and some have a brief description. There are no links or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[6]

The authors state they fix the parameters across all methods (sec 4.4). There are some notes throughout the work regarding the architecture, but an overview is missing. Its also not clear. A lot will have to be deduced from the provided examples to attempt reproduction, which will be quite some work.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Authors report average test accuracy over 50 samples with unclear variation. They apply five fold cross validation to select the best performing. The strategy seems to vary per experiment, which will require some carefull reading. Parameters seem to be clearly documented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
