
## Detecting Change Intervals with Isolation Distributional Kernel
Yang Cao, Ye Zhu, Kai Ming Ting, Flora D. Salim, Hong Xian Li, Luxing Yang, Gang Li
Keywords: 
JAIR/2024/Proceedings/15762 - Detecting Change Intervals with Isolation Distributional Kernel.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the introduction (https://github.com/IsolationKernel/iCID). In the readme they state some details regarding the development. No installation instructions. The code can use more comments. Pseudo code given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(8/8)

The authors use benchmark datasets, 6 real world (Yahoo-16, USC-HAD, Google-Trend, Well_Log, Weather, HASC each with description and direct links) and two synthetic datasets (Provided in the implementation) taht they generated and provide parameter values on and some details and statistics in figure 1/6. The generation code is not provided. More details in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state a few parameters in algorithm 1/2 and sec 5.2., and the authors state the parameter grids in table 3. The exact selection procedure is not stated, the best window value for HASC and USC-HAD is stated in table 4 but the other selected values are unclear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors method does not require training, thus split is not applicable. Results are on entire datasets. The authors measure value and score (which seems to be F1-score?) but its not really clearly stated what these are. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on time series data.
