
## Unlocking Slot Attention by Changing Optimal Transport Costs
Yan Zhang, David Zhang, Simon Lacoste-Julien, Gertjan Burghouts, Cees Snoek
Keywords: 
ICML/2023/Proceedings/24697 - Unlocking Slot Attention by Changing Optimal Transport Costs.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/davzha/MESH). In the readme they provide instructions on how to prepare the data (seperate readme). Furthermore they state how to run the code for 4 experiments. There is an installation file (requirements.txt). There is very few comments in the code. The repository structure may seem large at first but is actually quite small.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors provide 2 direct links for two datasets in the implementation. They provide citations on these and describe them with more details in appendix F.4. Statistics on them are shallow. They also use a synthetic generation for which they provide code and details on in section 5.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors refer to a different work regarding the hyperparameters in appendix F3. Details on this are quite obscure.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors report the results over 5 random seeds with mean and standard deviation. The metric is precision. In table one its RMSE and they show results as median instead (no variation) over various generator parameter settigns. There is no specification on training or testing set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5 ]

Requires expertise on slot attention, sinkhorn and object detection.
