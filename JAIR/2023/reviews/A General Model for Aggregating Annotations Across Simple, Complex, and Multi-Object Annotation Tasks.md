
## A General Model for Aggregating Annotations Across Simple, Complex, and Multi-Object Annotation Tasks
Alexander Braylan, Madalyn Marabella, Omar Alonso, Matthew Lease
Keywords: 
JAIR/2023/Proceedings/14388 - A General Model for Aggregating Annotations Across Simple, Complex, and Multi-Object Annotation Tasks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the introductions, footnote 1 (https://github.com/Praznat/annotationmodeling). In the readme they describe the repository and link a second paper describing it more formally. They give examples, including code examples. There is an installation file available ('requirements.txt'). The code needs better comments. There are quite a lot of files and it could use an index. Extensive pseudo code available. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(12/12)

The authors state they use simulated datasets and real data, the tasks are explained in 8.1.1. The real datasets are listed in 8.1.2 with a description and citation but most are not present in implementation, statistics are summarised in table 12. In 8.1.3 they describe synthetic data generation, code is available in the implementation and some data seems to be present in the data folder, different settings are visualised in figure 14.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors define the parameter values of gamma, delta and gamma of eq 8 based on results from a previous work. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state and describe the metrics in 8.1.4. The results are averaged in figure 15 over the entire dataset, as well as table 11. Results of the real dataset are over the entire dataset. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on NLP.
