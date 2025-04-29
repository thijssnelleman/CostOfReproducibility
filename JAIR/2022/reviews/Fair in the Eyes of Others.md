
## Fair in the Eyes of Others
Parham Shams, Aurélie Beynier, Sylvain Bouveret, Nicolas Maudet
Keywords: 
JAIR/2022/Proceedings/13778 - Fair in the Eyes of Others.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use the Spliddit dataset and provide a citation and a description of the dataset, as well as synthetic experiments on uniformly distributed data but describe it only very briefly and do not provide the implementation. Statistics are provided in table 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors discuss a concentration parameter but this is not clearly defined. It is varied over in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure the number of SM-app EF (defined on page 918) / value of k/n instances over the value of concenctration and number of agents and objects. The results are presented as boxplots. Concentration is a parameter of the agents. In the table the authors measure the mean k/1 and time in seconds, but the other metrics are not completely clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on envy-freeness.
