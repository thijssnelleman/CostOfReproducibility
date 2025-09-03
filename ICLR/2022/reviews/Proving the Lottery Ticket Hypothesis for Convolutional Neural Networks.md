## Proving the Lottery Ticket Hypothesis for Convolutional Neural Networks
Arthur da Cunha, Emanuele Natale, Laurent Viennot
Keywords: 
ICLR/2022/Proceedings/5981 - Proving the Lottery Ticket Hypothesis for Convolutional Neural Networks.pdf
Project URL: https://openreview.net/attachment?id=Vjki79-619-&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the reproducibility statement (https://github.com/AInnervate/cnnslth). The authors provide information on how to install the dependencies and how to run the code in the readme, as well as where stored information is found and used. Code has ok comments, but the readme is rather shallow.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use MNIST (provided citation) and Fashion-MNIST (Citation provided). Datasets download automatically in the code. No much other information given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors use a CNN for analysing their theory, and base their archtiecture and settings on a previous work motivated by its size (citation provided). They state other HP values and cite a paper for explaining the values to be default. A structured overview of these values is missing however.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure relaitve weight error and output error over various sample sizes on the train and test sets provided by the datasets. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
