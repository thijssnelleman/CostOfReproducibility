
## Convergence for nonconvex ADMM, with applications to CT imaging
Rina Foygel Barber, Emil Y. Sidky
Keywords: 
JMLR/2024/Proceedings/210831 - Convergence for nonconvex ADMM, with applications to CT imaging.pdf
Project URL: https://github.com/rinafb/ADMM_CT

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website (https://github.com/rinafb/ADMM_CT). In the readme they provide an overview of which notebook accompanies which experiment. There are no installation instructions. The notebooks have a lot of comments and descriptions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors conduct experiments for a CT task in section 5 which is simulated. The generator is provided and the settings are described in 5.2 and the notebook. In 4.3 they conduct an experiemnt on the sparse quantile regression problem (synthetic) and the generator with parameters are also provided in the notebook and 4.3. The latter problem is only very briefly described.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The parameters for optimization are stated in each notebook in a seperate block. The authors evaluate the method over various sigma values in each experiment (grid). The parameters are stated in algorithm 1. Only the sigma parameter is marked as a true parameter in the notebooks and the evaluated grids are specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure loss and RMSE in sec 4.3 over single runs with various values of sigma. In 5.2. they prsent photon spectral density over energy units (problem specific, defined in 5.1) as well. No aggregation, variation or split applicable. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on ADMM and simulated CT data.
