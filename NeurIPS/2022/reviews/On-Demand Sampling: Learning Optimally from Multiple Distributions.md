
## On-Demand Sampling: Learning Optimally from Multiple Distributions
Nika Haghtalab, Michael Jordan, Eric Zhao
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/1931 - On-Demand Sampling: Learning Optimally from Multiple Distributions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation in the supplementary materials (https://openreview.net/attachment?id=FR289LMkmxZ&name=supplementary_material) and on GitHub on the open review page (https://github.com/ericzhao28/multidistributionlearning?utm_source=catalyzex.com). In the readme they state how to run the code and acknowledge code they base theirs on with a link. There are no installation instructions. The code can use better comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use the Waterbirds, MultiNLI and CelebA dataset and provide citations on them in section 6. No other details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the models are trained in three settings: Standard, Strong regularization and early stopping. The exact parameters can be found in the experiments file of the implementation (structured). The acquisition of these values is not clear (What is 'standard'? How was strong and early determined?).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate single models, the metrics are worst-group and average accuracy. Results are on the test split, and they refer to the static split of each dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in on demand sampling and multi distributions.
