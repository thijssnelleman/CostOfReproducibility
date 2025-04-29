
## ADBench: Anomaly Detection Benchmark
Songqiao Han, Xiyang Hu, Hailiang Huang, Minqi Jiang, Yue Zhao
Keywords: 
NeurIPS/2022/Proceedings/55709 - ADBench: Anomaly Detection Benchmark.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in contributions point four of the introduction (https://github.com/Minqi824/ADBench). In the readme they describe and introduce the method, installation instructions, examples, description with statistics of included datasets, included algos with lots of detail. The code is well documented with comments. There are seperate readmes for the data set directory making the structure overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(57/57)

The authors provide download links for 10 datasets and statistics for 57 in the implementation as well as appendix B where they include descriptions and citations and statistics over all the datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors benchmark other works on their work and refer for the hyperparameter choice to the original work. They are informally stated per method in appendix B but also structured present in their code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Data set split given in 4.1. Experiments are repeated three times and averaged. Metrics are Avg rank, AUCROC, time in seconds as metrics. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on anomaly detection.
