
## Incremental Event Calculus for Run-Time Reasoning
Efthimis Tsilionis, Alexander Artikis, Georgios Paliouras
Keywords: 
JAIR/2022/Proceedings/12695 - Incremental Event Calculus for Run-Time Reasoning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 (https://github.com/eftsilio/Incremental_RTEC). In the readme they describe how to run the code, refer to papers for documentation, list related software. There are no installation instruction. The code has good comments and the structure is overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/2)

There are data downloaders in the implementation for the french maritime activity dataset and a link in footnote 6. The data is describe in detail in 5.2. with citations and describe how they synthesise parts of the data for the task in 5.2.1 with parameter values of the gamma distribution given. The authors briefly describe a second dataset in 5.2.2 but it is a private dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method uses a sliding windows as semantic parameter, and is varied in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure average time in seconds over a window in hours/SDEs (Simple derived events) and present procentual improvements. They vary the total recognition time, fluent improvement and interval manipulation construct improvement for the synthetic data. A lot of this requires data/task specific expertise.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on run-time reasoning.
