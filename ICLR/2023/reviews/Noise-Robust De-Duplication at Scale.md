## Noise-Robust De-Duplication at Scale
Emily Silcock, Luca D'Amico-Wong, Jinglin Yang, Melissa Dell
Keywords: 
ICLR/2023/Proceedings/11067 - Noise-Robust De-Duplication at Scale.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors publish a new dataset and run existing methods to benchmark them and publish it (https://github.com/dell-research-harvard/NEWS-COPY). Readme contains installation notes, how to download data and link to pretrained models. Code is well documented.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors publish a new dataset called NEWS-COPY and provide extensive details. Download link provided. Authors also use C4 which is cited described and linked. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors publish a dataset, methods shown are not theirs thus N/A.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Data set split shown in table 1. The authors measure computational efficiency (GPU/CPU time), and ARI (explained in introduction) but the results are very concise adn will take some decoding to understand how to reconduct.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
