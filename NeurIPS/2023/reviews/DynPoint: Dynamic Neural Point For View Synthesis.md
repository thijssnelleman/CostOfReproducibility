
## DynPoint: Dynamic Neural Point For View Synthesis
Kaichen Zhou, Jia-Xing Zhong, Sangyun Shin, Kai Lu, Yiyuan Yang, Andrew Markham, Niki Trigoni
Keywords: 
NeurIPS/2023/Proceedings/70705 - DynPoint: Dynamic Neural Point For View Synthesis.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a link to their implementation in the paper. Overview is given in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use Nvidia, Nerfie, HyperNeRF and Iphone datasets (all citations provided). In the supplementary material the atuhors describe the datasets in great detail. Statistics are lacking. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The network structure is discussed in section 1 of the supplementary material, but real HP overview is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors use PSNR, LPIPS, mPSNR and mSSIM as metrics which are described in detail in supplementary 3.1. The results are averaged but its unclear over what. The evaluation is over test data but its not clearly specified how this is done per dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on CV.
