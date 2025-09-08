## Generalization in diffusion models arises from geometry-adaptive harmonic representations
Zahra Kadkhodaie, Florentin Guth, Eero Simoncelli, Stéphane Mallat
Keywords: 
Award: Outstanding Paper Award
ICLR/2024/Proceedings/818 - Generalization in diffusion models arises from geometry-adaptive harmonic representations.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide their implementation at the bottom of the first page (https://github.com/LabForComputationalVision/memorization_generalization_in_diffusion_models). The readme contains a high level index of the repo, a list of requirements, summary of the method. The code has okay comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

CelebA (citation provided, no other details), synthetic dataset called Cα class (citation provided, described in appendix E, generator provided in code, parameters unclear).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values and choices in appendix A.2. Some are unmotivated. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

PSNR as metric (not explained), results are single runs on both train and test set. Split not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
