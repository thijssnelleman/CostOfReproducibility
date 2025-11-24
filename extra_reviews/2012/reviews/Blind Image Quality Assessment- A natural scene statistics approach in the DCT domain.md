## Blind Image Quality Assessment- A natural scene statistics approach in the DCT domain
M.A. Saad, A. C. Bovik, C. Charrier
Keywords: Discrete Cosine Transform (DCT), generalized Gaussian density, natural scene statistics, no-reference image quality assessment
extra_reviews/2012/Proceedings/Blind Image Quality Assessment- A natural scene statistics approach in the DCT domain.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors state in the introduction that their implementation is published on their group website. After a small search; they link it in their software publications (http://live.ece.utexas.edu/research/Quality/BLIINDS2_release.zip). There is no readme, installation instructions or how to run. There are few comments. Structure is simple but the code will take some effort to understand due to the lack of meta information.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use the Live IQA database and TID2008, and describe it very briefly in sec 3.a. and sec. 5. Citation provided with link. Details/statistics lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors define the formulae of the parameter values in sec 2.A. Some values can also be extracted from the implementation but is less structured that could have been. Overall the values seem to be there, but it will take some effort to determine each per experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors use an 80/20 and 90/10 split on Live IQA dataset / TID2008 dataset. The authors measure SROCC and LCC correlations among others but provide little information (assumed the reader knows this). Authors report boxplots over 1000 trials. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
