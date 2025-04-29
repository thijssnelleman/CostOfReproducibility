
## Learning Pollution Maps from Mobile Phone Images
Ankit Bhardwaj, Shiva Iyer, Yash Jalan, Lakshminarayanan Subramanian
Keywords: Humans and AI: Computational Sustainability and Human Well-Being, Computer Vision: Applications, Computer Vision: Interpretability and Transparency, Machine Learning: Applications, Machine Learning: Ensemble Methods, Machine Learning: Explainable/Interpretable Machine Learning, Multidisciplinary Topics and Applications: Computational Sustainability, Multidisciplinary Topics and Applications: Sustainable Development Goals
IJCAI/2022/Proceedings/0697 - Learning Pollution Maps from Mobile Phone Images.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present a link to their implementation (https://github.com/ankitbha/pollution_with_images). They provide an index on the repository and the code, explain how to run the entry point, and provide notebooks that can run the code. An environment file is given regarding the installation. The code has almost no comments. An architecture diagram is given in figure 3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors present their own dataset, and state details and examples on it in section 3.1. There are a few sources presented they used to collect this data (The data is seemingly not completely produced by the authors) with a few links provided. The full data set is linked in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The hyperparameter values of the methods evaluated (not their own method rather they apply different methods to the task presented) are hard coded in the implementation. Some details are specified in section 4, but a full overview is missing. This increases the effort to understand the exact values used for each experiment. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use MAE as a metric and present it with a standard deviation over the test set in table 1. The data set split is specified in section 4. The results are seemingly single runs, based on the tables and notebooks in the implementation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience with CV and ensembling.
