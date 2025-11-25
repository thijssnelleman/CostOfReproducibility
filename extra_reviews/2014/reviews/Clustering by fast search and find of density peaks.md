## Clustering by fast search and find of density peaks
Alex Rodriguez, Alessandro Laio
Keywords: 
extra_reviews/2014/Proceedings/Clustering by fast search and find of density peaks.pdf
http://www.sciencemag.org/content/344/6191/1492/suppl/DC1

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation in the supplementary material (https://www.science.org/doi/suppl/10.1126/science.1242072/suppl_file/1242072datas1.zip). The implementation consists of a single matlab file, there are no installation instructions and there are very few comments. The authors do provide an example data file, which is straightforward to run based on the interactive terminal statements in the code. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors provide a data set in their code. They use; data set from Gionis, H. Mannila, P. Tsaparas, an x-ray features for three types of wheat seeds from M. Charytanowicz et al. (2010), dataset from H. Chang, D.-Y. Yeung (2008), Olivetti Face Database. All datasets are cited, but descriptions are very brief. There are no direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors state that their method does not require any parameters. This is also easily confirmed by their supplied code.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors evaluate their method on the datasets. Single run, no splits applicable. The authors measure number of elements over data set size N, as well as local density (r, formula defined and explained) over minimum distance to the larger neighbour (d, formula provided and explained), and number of points over misclassification percentage. Other results are qualitative rather than quantitative. Error bars shown are standard errors over the dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[2]

-
