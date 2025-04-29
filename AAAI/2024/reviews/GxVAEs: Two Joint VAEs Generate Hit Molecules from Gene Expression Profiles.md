
## GxVAEs: Two Joint VAEs Generate Hit Molecules from Gene Expression Profiles
Chen Li, Yoshihiro Yamanishi
Keywords: ML: Deep Generative Models & Autoencoders, APP: Other Applications
Award: Outstanding paper award
AAAI/2024/Proceedings/30357 - GxVAEs: Two Joint VAEs Generate Hit Molecules from Gene Expression Profiles.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a source for their implementation (https://github.com/naruto7283/GxVAEs). In their paper they note some experimentation execution details, and hyperparameter values. In their repository, the authors show a detailed overview of the implementation. They state the objective and contact details in their readme. They have a requirements file with installation instructions, and short file description for the repository directories. The authors provide exact instructions on how to re-run the experiments, including training, testing, otuput data generation and metric calculations. The code is properly commented, thus the flow of the process is easy to follow in general.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/2)

The authors use two data sets for their experiments, each of which has a description and citation, and a few statistics. One data set was extracted from another, which is explained. One data set is directly available in the implementation source. Where the second data set is to be found is not directly linked.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors give the hyperparmeter values per task, but do not specify how these values were acquired. Any missing or needed values could be extracted from the implementation, but a unified file representing all HP's is missing so this will take some effort.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors clearly explain their evaluation metrics, and refer to their linkexd appendices regarding coefficient calculations. The table results seem to indicate single run evaluation, and more details can be extracted from the implementation docs, but a clear summary on the procedure is missing.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The presented method is cross domain with biology, specifically genome biology and its implacations on human meidcal states/diseases. To fully understand the data, this cross domain knowledge is required. The method has many layers and steps, and makes use of Generative AI (VAE's, which are relatively accesible but do require more experience) in two layered steps.
