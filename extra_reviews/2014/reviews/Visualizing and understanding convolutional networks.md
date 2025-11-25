## Visualizing and understanding convolutional networks
Matthew D. Zeiler, Rob Fergus
Keywords: 
extra_reviews/2014/Proceedings/Visualizing and understanding convolutional networks.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. An overview is given in figure 1 and 3.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use ImageNet 2012 and 2013 and provide a citation. They also use Caltech-101, Caltech-256 and PASCAL VOC 2012. Descriptions are limited and there are no direct download links. High level statistics provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors describe their architecture in figure 3. Training details are stated in section 3 in text with parameter values. Motivations are given in section 4. As this method serves as an input for their visualisation, acquisition and budget is less applicable.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure (top-k) accuracy and classification error rates. The authors use the static splits of the data sets. They also use 5 folds for post-training on caltech-101. Variation unit not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
