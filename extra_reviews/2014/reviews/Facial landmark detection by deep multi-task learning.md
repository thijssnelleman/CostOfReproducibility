## Facial landmark detection by deep multi-task learning
Zhanpeng Zhang, Ping Luo, Chen Change Loy, Xiaoou Tang
Keywords: 
extra_reviews/2014/Proceedings/Facial landmark detection by deep multi-task learning.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. An overview is given in figure 3, an a high level one in figure 2. No technical details provided, except for a few runtime measurements/insights.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

FLD dataset (Download link provided) from Sun et al. (2013), and their own dataset (Download link provided) called MTFL. Descriptions are very short and statistics few.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[5]

The authors state hyperparameters in text in section 3. The architecture is given in figure 3. Acquisition not specified and structured overview is missing. It will need to be verified that all necessary parameter values are there, which is a bit of work on its own.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure mean error and failure rate and explain the metrics. They train on MTFL and evaluate on specified subsets of FLD. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
