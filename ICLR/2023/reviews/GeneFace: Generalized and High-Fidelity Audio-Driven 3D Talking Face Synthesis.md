## GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis
Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu, Jinzheng He, Zhou Zhao
Keywords: 
ICLR/2023/Proceedings/12262 - GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis.pdf
Project URL: https://openreview.net/attachment?id=YfwMIDhPccD&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a project page with examples, where they link their implementation (https://github.com/yerfor/GeneFace). The authors provide in the readme a seperate installation guide, where to download checkpoints and how to use the code with it, how to run code, where to find data prep scripts, where to find model training scripts, acknowledgements for repos used to build the implementation. The structure is huge and can use an index more detailed than currently provided. Code has ok comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use LRS3-TED and two datasets of previous works. Citations are provided but few details given. Links in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values given in table 4 of appendix B. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

The authors measure FID, LMD, Sync, FID(OOD), Sync(OOD) which are explained in 4.3 and results are single runs. They conduct a user study which they present with 95% CI (agg not specified). Data split etc not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
