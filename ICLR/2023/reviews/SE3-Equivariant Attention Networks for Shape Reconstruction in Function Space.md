## $\mathrm{SE}(3)$-Equivariant Attention Networks for Shape Reconstruction in Function Space
Evangelos Chatzipantazis, Stefanos Pertigkiozoglou, Edgar Dobriban, Kostas Daniilidis
Keywords: 
ICLR/2023/Proceedings/10857 - SE3-Equivariant Attention Networks for Shape Reconstruction in Function Space.pdf
Project URL: https://openreview.net/profile?id=~Evangelos_Chatzipantazis1

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide their implementation. Overview of the method in figure 2, 3. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(1/2)

The authors use ShapeNet (citation provided, no link, details are few) and construct a dataset called Seismic dataset, on which they provide details how it was constructed from shapenet but not the actual dataset or the code to do so.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors summarise the architecture and hyperparameter values in text in appendix A.2. No structured overview, no acquisition specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors explain the metrics in detail in appendix A.1. The authors train the model on a subset of shapenet, based on a procedure of a previous work which they cite but direct details are not given. They also evaluate on seismic. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
