## Evaluating Disentanglement of Structured Representations
Raphaël Dang-Nhu
Keywords: 
ICLR/2022/Proceedings/6441 - Evaluating Disentanglement of Structured Representations.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[7]

There is an overview in figure 1 of the method and figure 2 with a toy example. Pseudo code in algorithm 1. Section 5 states they use public Pytorch implementations for the input methods. No implementation seems to be given although they do provide alot of details of where they sourced other methods implementations from they rely on.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use CLEVR6 and Multi-dSprites and provide citations on them with a briefy description and some more information is available in the appendix but link/extensive information is missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

Hyperparameter values of input methods can be found in appendix C and they base the values mostly on the original work except for a few, using other related work. They also use GECO to tune HP beta. Their own method is seemingly parameter free.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors state how training datasets/evaluation datasets are created in C.3. / C.4. The authors measure object-level disentenglement and ARI/mSC but most metrics remain unexplained (required expertise). Results are prsented over three seeds with mean and standard error.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
