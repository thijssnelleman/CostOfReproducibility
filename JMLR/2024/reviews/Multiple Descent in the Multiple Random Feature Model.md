
## Multiple Descent in the Multiple Random Feature Model
Xuran Meng, Jianfeng Yao, Yuan Cao
Keywords: 
JMLR/2024/Proceedings/221389 - Multiple Descent in the Multiple Random Feature Model.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the references (https://github.com/XuranMeng/Multipledescent/blob/main/onlinesupplementary.pdf). In the readme they state what their repository contains, regarding what function does what. They also state where the experiments code can be found. The code has okay comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use simulations for their experiments. The simulation and its parameters are stated in section 4/5. The generator is present in the code. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors evaluate DRFM with various activation functions on the data. The parameters regarding the problem and functions are clear. It is not clear what parameters are considered for DRFM/MRFM.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use generated training and test data and state their generations in section 4. It is evaluated over 'risks' for which they refer to a previous work and define in formula 2.3. results are single runs. It is not clear on which dataset they present the evaluation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise in multiple descent and random feature models.
