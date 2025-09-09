## A Restoration Network as an Implicit Prior
Yuyang Hu, Mauricio Delbracio, Peyman Milanfar, Ulugbek Kamilov
Keywords: 
ICLR/2024/Proceedings/17467 - A Restoration Network as an Implicit Prior.pdf
Project URL: https://openreview.net/attachment?id=x7d1qXEn1e&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors state in the reproducibility statement that the code is available in the supplementary materials (https://openreview.net/attachment?id=x7d1qXEn1e&name=supplementary_material). In the readme they state how to install dependencies, where to download the code and the entry point code of the experiments. Code has good comments. The code does not have any parameters so the examples in the readme suffice.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(6/6)

Set3c, Set5, CBSD68, McMaster, DIV2K (citation) and Flick2K (Citation). No other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[7]

The authors state they finetuned 2 HPs in 5.2. on one dataset and re-used the values for all others but not how. There are values available in the code but its not clear which value belongs to which experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Two datasets used for training, others for evaluation. Authors measure PSNR↑/LPIPS↓ (not explained), single runs/seed (same seed re-used for all methods).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
