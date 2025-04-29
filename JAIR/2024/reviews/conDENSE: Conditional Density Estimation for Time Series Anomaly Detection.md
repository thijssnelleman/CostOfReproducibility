
## conDENSE: Conditional Density Estimation for Time Series Anomaly Detection
Alex Moore, Davide Morelli
Keywords: 
JAIR/2024/Proceedings/14849 - conDENSE: Conditional Density Estimation for Time Series Anomaly Detection.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors state a few libraries used and link two repositories used for implementation. High level overview given in figure 1. They state they used TensorFlow as a framework. No other details provided.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use 4 real world datasets in 3.6.1, give statistics on them in table 1 and describe them, citations are provided. The authors use synthetic datasets in 3.6.2. and provide details on them in table 5 of the appendices. They cite the source they used to generate the data, and name the tool GutenTag, but details on this process are missing. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the HPs of their method in table 3. The authors state some notes on HPO but details are unclear. Selected values are given per dataset.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state evaluation metrics in 3.7. The authors measure mean/median and standard deviation of training time in table 4, population not specified. The datasets have static splits. For some results its not specified on which split they report results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on time series data and anomaly detection.
