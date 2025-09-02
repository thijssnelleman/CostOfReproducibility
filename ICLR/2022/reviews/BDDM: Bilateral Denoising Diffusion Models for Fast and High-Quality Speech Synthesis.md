## BDDM: Bilateral Denoising Diffusion Models for Fast and High-Quality Speech Synthesis
Max W. Y. Lam, Jun Wang, Dan Su, Dong Yu
Keywords: 
ICLR/2022/Proceedings/6010 - BDDM: Bilateral Denoising Diffusion Models for Fast and High-Quality Speech Synthesis.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the abstract (https://github.com/tencent-ailab/bddm). The readme has an overview on the method, change list, how to get started including installation, how to download and prepare data, training example and how to change configuration, how to produce data for analysis, and acknowledgements. The code contains a lot of comments. Psuedo code given in algorithm 1-4.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

Readme of implementation contains a link to LJSpeech dataset. The dataset is cited in the paper with a brief description. They also use the VCTK dataset but no link is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors conducted a grid search (values reported) for part of the parameters and report more values in text in B.2. There are also a few structured files available in the implementation. In general all information seems to be there, but it will require some thorough reading to understand what procedure was used to acquire which value.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors refer for the training split to a previous work. More details are given in appendix C on this. The results are presented with 95% CI, but aggregation is not specified (mean implied?). It is also not stated over what the variation / aggregation is done.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
