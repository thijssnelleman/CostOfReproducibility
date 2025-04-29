
## Local Differential Privacy Meets Computational Social Choice - Resilience under Voter Deletion
Liangde Tao, Lin Chen, Lei Xu, Weidong Shi
Keywords: Multidisciplinary Topics and Applications: Security and Privacy, Agent-based and Multi-agent Systems: Computational Social Choice
IJCAI/2022/Proceedings/0547 - Local Differential Privacy Meets Computational Social Choice - Resilience under Voter Deletion.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors share a link to their implementation (https://github.com/polyapp/poldp). The readme is nearly empty. The code structure is unclear, and the files seem to have very few comments. They also publish data sets here. In addition to that, alot of files have unindicative names, and/or are not readable. This worsens the usability of the implementation substantially. It is also hard to verify whether all the needed code is actually presented.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7] 

(1/2)

The authors use a real-world data set, which they provide citations on and is available in the implementation. The authors state they generate the 'true type of each voter' with two methods, and briefly describe how this generation is done (one using the previously mentioned data set). It is not clear where in the implementation this generation process can be found. More data files can be found in the implementation docs, but the names are not informative.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state three parameter values in section 5, which were introduced in previous sections. These values are not considered as method configurations. Then the authors evaluate the efficiency of the method over varying values of two parameters. These are rather analysis of the impact of varying these values than algorithm configurations.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the method under varying parameters and evaluate under percentages and 'PoLDP'. Problem parameters are stated at the beginning of section 5. The experiment requires domain/problem knowledge to understand what is being measured. The authors state they show average and standard deviation for aggregation data. This data population is created by varying the epsilon parameter over the range (0.00 0.01 ... 0.49, 5.00), e.g. population of 500.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires domain knowledge on computational social choice, the problem (resilience of a voting system).
