## Topological Graph Neural Networks
Max Horn, Edward De Brouwer, Michael Moor, Yves Moreau, Bastian Rieck, Karsten Borgwardt
Keywords: 
ICLR/2022/Proceedings/6389 - Topological Graph Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the Reproducibility Statement (https://github.com/BorgwardtLab/TOGL). The readme has a quickstart for installation and how to run, an explanation of the parameters and how to use them, where logs will be placed, and how to use various dataset and generate the synthetic ones. They also include the code to create the plots. The code has ok comments but the repository is quite large and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

The authors use synthetic datasets in 5.2, named Cycles, Necklaces and provide the code and how to generate the dataset in the implementation. The authors also use DD, Enzymes, Proteins, MNIST and MOLHIV. Citations are provided but descriptions are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors use architectures of previous works and inject their method (layer) into it, motivating it with an explanation in appendix H. They also provide a few details in appendix D including specific values and strategies but a full overview is missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors present the results on the test set and use accuracy reported over different fold with mean and standard deviation over 5 or 10 cross fold validation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
