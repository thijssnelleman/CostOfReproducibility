
## Privacy Auditing with One (1) Training Run
Thomas Steinke, Milad Nasr, Matthew Jagielski
Keywords: 
Award: Outstanding Paper
NeurIPS/2023/Proceedings/2819 - Privacy Auditing with One (1) Training Run.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share the implementation. Various pieces of pseudo code available.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The atuhors use CIFAR-10. No details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

For most parameters the authors refer to another work. For their own parameters (K+ and K-) they evaluate the method on various values and report the highest. These values are not specified. Parameter Epsilon is given through theoretical analysis.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors evaluate the method with 95% confidence. aggregation not given. Population not clear. Test set not applicable. Epsilon is a subfield specific metric but its not defined.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on privacy auditing.
