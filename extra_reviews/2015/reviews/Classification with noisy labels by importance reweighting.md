## Classification with noisy labels by importance reweighting
Tongliang Liu, Dacheng Tao
Keywords: Classiﬁcation, label noise, noise rate estimation, consistency, importance reweighting
extra_reviews/2015/Proceedings/Classification with noisy labels by importance reweighting.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors do not provide their implementation. There is no pseudo code or diagrams.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

The authors use synthetic data (8.1), UCI benchmarks (8.2): Breast cancer, Diabetes, German, Heart, Image and Thyroid. Descriptions are lacking, no citations, or direct links. The synthetic parameters are provided per result.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors evaluate the method with varying noise rates. The rates are provided per experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors randomly split each dataset 75/25 for train test and report mean and standard deviation. Three-fold cross validation was used on the training set if tuning was needed (Not theirs).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
