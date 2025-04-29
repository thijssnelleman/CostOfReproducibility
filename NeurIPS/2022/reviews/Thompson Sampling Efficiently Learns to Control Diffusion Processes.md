
## Thompson Sampling Efficiently Learns to Control Diffusion Processes
Mohamad Kazem Shirani Faradonbeh, Mohamad Sadegh Shirani Faradonbeh, Mohsen Bayati
Keywords: 
NeurIPS/2022/Proceedings/54972 - Thompson Sampling Efficiently Learns to Control Diffusion Processes.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Implementation not given. Pseudo code in alg 1/2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The authors use a flight dataset and cite it. No other details provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the values of the pseudo code in the experiments in section 6. No acquisition specified. Due to the simplicity, no tabular overview required.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors run the method 1000 times and plot the percentage of stabalization over time. They also measure normalised squared estimation error (formula given). Data split not applicable. No variation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on thompson sampling and diffusion processes.
