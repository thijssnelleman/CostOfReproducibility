
## MultiVENT: Multilingual Videos of Events and Aligned Natural Text
Kate Sanders, David Etter, Reno Kriz, Benjamin Van Durme
Keywords: 
NeurIPS/2023/Proceedings/73710 - MultiVENT: Multilingual Videos of Events and Aligned Natural Text.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present a novel dataset in their method. The authors also introduce a new method (MultiCLIP) as a baseline. The authors link an implementation on the Audio conent in appendix B regarding tokenisation. The authors upload their code through the supplementary material. This directory is linked to a github repository which we extracted the link from (https://github.com/katesanders9/multiVENT). In the readme they state details on the dataset being released on hugging face, info on the repo, a detailed overview on the structure, how to navigate the data, how to install, how to prepare the data and sources they lean on. The code has few comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors introduce a novel dataset and provide details and statistics on it in table 6 and 7. In section 3 they describe the collection process and data types. They state the colelction process and sources in 3.2. Data statistics are illustrated in figure 2. A data analysis is conducted on the data set in sec 4. The data is publicly available on github and hugging face.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors use a previous method and apply it to their data. In sec 5.2. they cite this source and provide some minor details regarding the architecture. A configuration file can be found in the implementation. It would need to be checked if these are the used values per experiment.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors conduct experiments in sec 5. The metrics are straightforward. The results are single model. Train test split not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on multilingual video data (CV) and NLP.
