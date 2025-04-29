## On-Demand Sampling: Learning Optimally from Multiple Distributions
Nika Haghtalab, Michael Jordan, Eric Zhao
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/1931 - On-Demand Sampling: Learning Optimally from Multiple Distributions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

- The source code is provided as a supplemental material and as a link to Github repo in the appendix (https://github.com/ericzhao28/multidistributionlearning/tree/master). The README is short but straightforward; how to run the code is clearly explained in 3 lines. However, no examples are given and the authors do not walk the reader through the installation/set-up, but rather assume everything will work flawlessly if executed directly following their instructions. In my opinion, it is still a valid assumption because upon looking at these files one can relatively easily understand how the experiments are organised, so I do not increase the score further. In general, the authors refer to a previous work (Sagawa et al. 2019) for most of the things pertaining to experiments. This previous paper proposes a SOTA algorithm against which the authors compare their method.
- The code seems to be nicely organised, the repo is not difficult to navigate, the main files to run the experiments are rather self-explanatory. However, there are very little comments throughout the code. This increases the score by 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

- The authors use 3 datasets, all of which are public, with detailed descriptions, citations, but no statistics and without a direct link to them. Nonetheless, I was able to find online all three datasets in one additional click, following the respective citations, in which the direct links were provided but not directly in their work.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

- The authors use the identical experimental setup as (Sagawa et al. 2019), which is fully documented in their paper. If there are any differences in their setup, the authors clearly state them. The motivation behind this is that they compare their method with the method in the previous work (which is SOTA). All information regarding hyperparameter spaces and values are clearly described in the text, but the overview table was not provided (neither in the previous work); this increases the score by 1. No hyperparameter optimisation was performed, except for certain HPs in certain experiments; all values are taken as high-performing ones for the previous method. This increases the score by 1.


### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

- The experimental procedure seems to be very clear and easy to set up from scratch. There is clear information about metrics used, train/valid/test splits and how this is done, evaluation acquisition strategy (single training run for a certain budget of epochs per method). It is clear how the results are aggregated -- they are actually not due to the nature of the experiments. There is therefore no variance over the aggregation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

This is a theoretical paper, with relatively small-scale experiments to empirically support the theoretical claims. As such, in order to reproduce this paper in its entirety, including all the proofs etc, one needs significant expertise in multiple domains of AI/ML and superior mathematical skills to arrive to the same conclusions as the authors. or even check if the maths is correct. The empirical part is rather well-documented and would have a low cost, but due to the theoretical nature of the paper, I give it the total expertise-related cost of 9 (for me, 10 is really something out-of-this-world complex). 