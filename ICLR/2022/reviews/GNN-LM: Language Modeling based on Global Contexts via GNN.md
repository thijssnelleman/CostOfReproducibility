## GNN-LM: Language Modeling based on Global Contexts via GNN
Yuxian Meng, Shi Zong, Xiaoya Li, Xiaofei Sun, Tianwei Zhang, Fei Wu, Jiwei Li
Keywords: 
ICLR/2022/Proceedings/6501 - GNN-LM: Language Modeling based on Global Contexts via GNN.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in a footnote in the abstract (https://github.com/ShannonAI/GNN-LM). The implementation contains an overview of the results, installation requirements including a .txt file, notes on hardware, how to download and preprocess the datasets and models, and acknolwedgements. There are seperate scripts showing how to run the code. The structure is massive and needs indexing / cleanup. Some of the code has good comments but its not present everywhere.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors provide scripts for downloading the datasets in their code for enwik9, one billion and wiki103. They are described with citations in section 3 albeit brief and more details would be preferred.  

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[7]

Not all HP values are clear per experiment, althoug they are given in the code for Wiki103. in general, most information in this regard is missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors present the test set results with perplexity and bit per character with single runs. The authors seem to imply they use static splits from the datasets (section 4.2) although this is not completely clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
