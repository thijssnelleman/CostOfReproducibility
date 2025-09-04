## DreamFusion: Text-to-3D using 2D Diffusion
Ben Poole, Ajay Jain, Jonathan T. Barron, Ben Mildenhall
Keywords: 
Award: Outstanding Paper Award
ICLR/2023/Proceedings/506 - DreamFusion: Text-to-3D using 2D Diffusion.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their project page, but that does not contain the implementation. In The reproducibility statement the authors state that the code they build upon is publicly available through the MultiNeRF code repository and cite the paper. They state the model is not publicly available, but provide a schematic overview in figure 3 with details, and detailed pseudo code in appendix A, figure 7 and 8. The repository they reference is well documented and can serve as a good starting point. However, it will still require quite some adaptation.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use MS-COCO and provide a small description and citation. They use the CLIP model for training.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors explain and motivate the hyperparameters in appendix A.2. and provide sometimes grids overwhich they selected their values. A structured overview is missing, although the information is well organised.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use the validation set of MS-COCO and measure R-Precision (Citation provided, explained). Results are evaluated with 2 generation seeds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
