## Deep learning-based classification of hyperspectral data
Yushi Chen, Member, Zhouhan Lin, Xing Zhao, Gang Wang, Yanfeng Gu
Keywords: Autoencoder (AE), deep learning, feature extraction, hyperspectral data classiﬁcation, logistic regression, stacked autoencoder (SAE), support vector machine (SVM)
extra_reviews/2014/Proceedings/Deep learning-based classification of hyperspectral data.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a repository online to "guarantee you to reproduce the results" for this paper and one other (https://github.com/hantek/deeplearn_hsi). The authors provide detailed pseudo code in algorithm 1-3. Highly detailed schematics in fig. 1-5. Implementation details stated in III. A. The code has installation instructions, how to download datasets, and how to run the experiments from the paper.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two datasets; mixed vegetation site over Kennedy Space Center (KSC), and an urban site over the city of Pavia, Italy. Statistics provided in table 1/2 and visualisation in fig 7. Descriptions in VI. A. Dataset links in the readme of the repo.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The authors provide the parameters per dataset in their code, although this is hard coded in it does seem to be quite structured. The values are not motivated.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure accuracy and kappa's coefficient over 100 replications, presenting the mean value.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
