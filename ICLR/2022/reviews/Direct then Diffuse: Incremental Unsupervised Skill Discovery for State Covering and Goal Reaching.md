## Direct then Diffuse: Incremental Unsupervised Skill Discovery for State Covering and Goal Reaching
Pierre-Alexandre Kamienny, Jean Tarbouriech, sylvain lamprier, Alessandro Lazaric, Ludovic Denoyer
Keywords: 
ICLR/2022/Proceedings/6977 - Direct then Diffuse: Incremental Unsupervised Skill Discovery for State Covering and Goal Reaching.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[7]

Implementation not given. Overview in figure 1. Pseudo code with detailed explanation in algorithm 1 / section 3.4 and extensively in appendix B.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use environments (public): 2D mazes and continuous control problems (Ant, Half-Cheetah and Walker2d) and provide citations for them. Parameters not applicable.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values summarised in various lists per experiment in appendix C.2. The acquisition is not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors provide coverage metrics (maze) in table 2 but the aggreegation/variation is not completely clear and over what it is calculated. In the other figures this is more clear (average over 48 unknown goals) and they also record average success rate. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
