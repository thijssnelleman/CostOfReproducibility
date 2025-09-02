## Explainable GNN-Based Models over Knowledge Graphs
David Jaime Tena Cucala, Bernardo Grau, Egor Kostylev, Boris Motik
Keywords: 
ICLR/2022/Proceedings/5985 - Explainable GNN-Based Models over Knowledge Graphs.pdf
Project URL: https://openreview.net/attachment?id=CrCvGNHAIrz&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide their source code in the supplementary materials (https://openreview.net/attachment?id=CrCvGNHAIrz&name=supplementary_material). The readme provides information on the method and how they implemetned it, the required libraries, overview on the directory structure, what code is located where and where the output will be saved, extensive examples on how to run the code, and how to analyse the output for their study for many experiments. Much of the code is sourced from other works used in their study, and their own code has a lot of comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use FB15K-237, NELL-995, WN18RR datasets which are provided in the supplementary materials. Statistics for the  splits are given in table 1 and 3. Each is cited although the descriptions are rather short. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values are stated in section 4 in the text. A structured overview is missing. The values seem to be sourced from previous works (Not their own method that requires the HPs) but this is not completely clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The dataset splits are present in the supplementary materials. The authors measure precision, recall, accuracy, f1 score, AUC and training time in seconds for each method. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
