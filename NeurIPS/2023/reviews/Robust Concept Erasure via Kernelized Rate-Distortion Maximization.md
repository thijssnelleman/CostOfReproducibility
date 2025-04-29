
## Robust Concept Erasure via Kernelized Rate-Distortion Maximization
Somnath Basu Roy Chowdhury, Nicholas Monath, Kumar Avinava Dubey, Amr Ahmed, Snigdha Chaturvedi
Keywords: 
NeurIPS/2023/Proceedings/72139 - Robust Concept Erasure via Kernelized Rate-Distortion Maximization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/brcsomnath/KRaM). In the readme they state isntallation instructions, a link to a second readme for acquiring the datasets, and how to run the code with parameter explanation. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors explain how to download the datasets in the implementation, providing a link for Deepmoji dataset. UCI Crimes downloads automatically. Glove is present in the implementation. Generator for synthetic data given, and a kaggle challenge download link. The authors provide citations for DIAL, UCI Crimes, Jigsaw. The datasets are described in detail in appendix C.1. Statistics are too high level.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

HPs are discussed in appendix C.3. There they state they acquire the values of delta and sigma parameters which they set using a gridsearch over the development set but no budget/gird specified nor acquired values. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors explain the three metrics in sec 5. and C.2. Results are single run. Data set split not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on concept erasure.
