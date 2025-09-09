## A Variational Perspective on Solving Inverse Problems with Diffusion Models
Morteza Mardani, Jiaming Song, Jan Kautz, Arash Vahdat
Keywords: 
ICLR/2024/Proceedings/19583 - A Variational Perspective on Solving Inverse Problems with Diffusion Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in footnote 1 of the abstract (https://github.com/NVlabs/RED-diff). In the readme they state installation requirements, where to find which pre-trained model, explanation of the scripts and their parameters with examples on how to run, contact information. Code has few comments. Structure is large and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use ImageNet (cited) and downloads in the code. No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Authors state HP tuning for two parameters in sec 5 which seems to be missing budget. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Authors measure Kernel Inception Distance (KID, cited), LPIPS, SSIM, PSNR, and top-1 classifier accuracy. The authors use pretrained models and evaluate on ImageNet-1k validation subset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
