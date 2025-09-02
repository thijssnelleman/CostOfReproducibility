## Connectome-constrained Latent Variable Model of Whole-Brain Neural Activity
Lu Mi, Richard Xu, Sridhama Prakhya, Albert Lin, Nir Shavit, Aravinthan Samuel, Srinivas C Turaga
Keywords: 
ICLR/2022/Proceedings/6591 - Connectome-constrained Latent Variable Model of Whole-Brain Neural Activity.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the reproducibility statement (https://github.com/TuragaLab/wormvae). In the readme they state prerequisites for running the code, how to install dependencies, how they visualised the datasets, how to run the scripts to rerpdouce the experiments with an explanation of the parameters of the scripts and where the output is located. The code has a good amount of informative comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The implementation link contains various dataset files. The authors use a dataset called 'C.elegans' and provide a description in 3.1 with citation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The hyperparameters of the experiment are hardcoded into the main.py of the implementation. Some details are given in appendix A.5 in text. A general overview is missing a bit (Hard coded values make it difficult to oversee if this is all hps that were considered and will take some investigation to verify). Value acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report correlation coefficient, ELBO (evidence lower bound, not explained), loss and KL divergence with mean and standard error over the holdout set and the process is repeated four times with different initializations (Appendix A.4). It is stated how many samples are in the holdout from the total set, but not exactly which were used.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
