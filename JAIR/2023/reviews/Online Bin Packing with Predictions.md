
## Online Bin Packing with Predictions
Spyros Angelopoulos, Shahin Kamali, Kimia Shadkami
Keywords: 
JAIR/2023/Proceedings/14820 - Online Bin Packing with Predictions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in section 6.1, in footnote 1 (https://github.com/shahink84/BinPackingPredictions). In the readme they state the requirements and how to compile, and how to deploy / run the code and what input it requires. The code has good comments and the structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use two types of benchmarks. They use the weibull distribution, which they state the parameters on and provide the dataset for in the implementation with a description where they got it from. The second type is from the BPPLIB where they provide the same information on and citations (GI, Schwerin, Randomly_Generated, Hard28 and Wascher). Descriptions are a bit brief and more statistics would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate hybrid with a delta parameter on a grid of 5. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure number of bins over error eta which is defined in 6.2. The authors discusshow to average in 6.5.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on bin packing.
