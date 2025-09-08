## Efficient Edge Inference by Selective Query
Anil Kag, Igor Fedorov, Aditya Gangrade, Paul Whatmough, Venkatesh Saligrama
Keywords: 
ICLR/2023/Proceedings/11483 - Efficient Edge Inference by Selective Query.pdf
Project URL: https://openreview.net/attachment?id=jpR98ZdIm2q&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the introduction (https://github.com/anilkagak2/Hybrid_Models). The readme has an overview on the method including a video link, installation instructions and which code file is the entry point to run but with no details. Some parts of the code ahs good comments although the key pieces seem to be without. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use ImageNet, CIFAR-100 and IMDB, details and citations provided in appendix A. Links not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values listed in appendix A.6. in text. No structured overview or acquisition.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

The authors measure accuracy over various latencies in ms and various coverage percentages. Data split unclear. Results are single runs. Not clear on what part of the dataset is reported on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
