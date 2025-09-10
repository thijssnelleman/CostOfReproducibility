## Negative Label Guided OOD Detection with Pretrained Vision-Language Models
Xue JIANG, Feng Liu, Zhen Fang, Hong Chen, Tongliang Liu, Feng Zheng, Bo Han
Keywords: 
ICLR/2024/Proceedings/17453 - Negative Label Guided OOD Detection with Pretrained Vision-Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation link in the abstract (https://github.com/tmlr-group/NegLabel). The readme has installation instructions, download link to datasets and how to place them in the repository, descriptions on some files, and how to run the code entry point. The code has good comments. Structure is large and could use an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

ImageNet-1k, iNaturalist, SUN, Textures, Stanford-Cars, CUB-200, Oxford-Pet, Food-101 (All cited, link for first 4 in implementation). No descriptions or other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors state the HP values in text in A.1.1 and that they source the values from the previous works (default values). Structured overview missing. The authorss experiment with various gorup number values in appendix A.5.4. motivating their value. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Metrics stated in A.1.2. (AUROC, FPR95). The authors use ImageNet-1k for training and the rest for validation. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
