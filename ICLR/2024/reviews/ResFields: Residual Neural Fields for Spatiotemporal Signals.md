## ResFields: Residual Neural Fields for Spatiotemporal Signals
Marko Mihajlovic, Sergey Prokudin, Marc Pollefeys, Siyu Tang
Keywords: 
ICLR/2024/Proceedings/19108 - ResFields: Residual Neural Fields for Spatiotemporal Signals.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a project link where a link to the code is given (https://github.com/markomih/ResFields). The readme has an overview of the method, a seperate readme detailing installation, data preparation (including download), and how to run the code to reproduce their experiments. Code is well documented.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

Owlii (cited), bikes and cat (cited), Deforming Things (cited) and ReSynth (cited). Download links provided in the implementation. Descriptions are brief.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Authors provide HP values in text in appendix A.1. Not all values are motivated. Structured configuration files given in the implementation.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

L1 Chamfer distance (CD↓) and normal consistency (NC↓), PSNR↑, SSIM (latter two are standard according to the authors). Data splits unclear. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
