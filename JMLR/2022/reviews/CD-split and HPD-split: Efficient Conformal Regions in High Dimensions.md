
## CD-split and HPD-split: Efficient Conformal Regions in High Dimensions
Rafael Izbicki, Gilson Shimizu, Rafael B. Stern
Keywords: 
JMLR/2022/Proceedings/20797 - CD-split and HPD-split: Efficient Conformal Regions in High Dimensions.pdf
Project URL: https://github.com/rizbicki/predictionBands

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state a link to their implementation on JMLR and in section 7 (https://github.com/rizbicki/predictionBands). In  the readme they state a brief introduction, installation instructions and an example. Code has okay comments. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors conduct simulation studies in section 5, provide the formulae and the parameters + values, refer to which library they use for implementation with a citation. Data generation code available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state parameter tuning in 5.1. They evaluate the CD split over four different types of splitting and different partition sizes. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure average size, conditional coverage absolute deviation and present the results over 5000 runs, aggregation/variation not applicable.  In some results they do show variation but what it is and what its calculated over is not clear. Data split is not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires epxertise on conformal prediction.
