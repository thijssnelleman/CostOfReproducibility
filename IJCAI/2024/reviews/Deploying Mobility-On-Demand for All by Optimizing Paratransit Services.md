
## Deploying Mobility-On-Demand for All by Optimizing Paratransit Services
Sophie Pavia, David Rogers, Amutheezan Sivagnanam, Michael Wilbur, Danushka Edirimanna, Youngseo Kim, Philip Pugliese, Samitha Samaranayake, Aron Laszka, Ayan Mukhopadhyay, Abhishek Dubey
Keywords: Multidisciplinary Topics and Applications: General, Planning and Scheduling: General
IJCAI/2024/Proceedings/0822 - Deploying Mobility-On-Demand for All by Optimizing Paratransit Services.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/smarttransit-ai/ijcai-deploying-mobility-on-demand). Here they describe their method, explain the directory structure and the code, setup instructions and how to start. The code is well documented. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/2)

The authors use a real world data set, which is private due to privacy reasons. They describe the data set in 4.1, and the features it contains. Statistics on the data sets are also provided, albeit only a few. The authors present synthetic data in their implementation docs. The authors also cite two other data sets they used for the task with citations. However none of the synthetic data is used for the experiments, thus a comparison would have to be defended based on the private data descriptions. These descriptions are quite complete, but the acquisition would still be a big effort.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on the definition and the implementation, both the online and offline method is parameterfree. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state their experiment set up in section 4.1. The method does not have a training procedure. The authors show their experiments with various percentages of known requests. Each experiment can easily be checked in the implementation notebooks. The authors also do a realworld pilot with their method which they detail in section 5.1. The metrics are accuracy and absolute numbers (standard), and two task specific metrics which acronyms they explain. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires some experience with AI planning, and with the mathematics describing the problem statement and solution space.
