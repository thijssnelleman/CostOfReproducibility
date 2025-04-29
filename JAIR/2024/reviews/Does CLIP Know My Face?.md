
## Does CLIP Know My Face?
Dominik Hintersdorf, Lukas Struppek, Manuel Brack, Felix Friedrich, Patrick Schramowski, Kristian Kersting
Keywords: 
JAIR/2024/Proceedings/15461 - Does CLIP Know My Face?.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors publish their implementation online and link it in footnote 2 in section 3.2 (https://github.com/D0miH/does-clip-know-my-face). In the readme they state a detailed description of the method, how to run the experiments, where to download pre-trained models, and image credits. There is an installation requirements file present. The structure is large and needs an index, code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use LAION, CC3M and FaceScrub datasets (citations provided) and are described with some statistics. The authors also state how the datasets were filtered for their application, code on this is available. Link in the readme for the CC3M dataset, but not for the other 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameter values in Appendix D. They refer to a previous paper for acquisition, and as this these parameters are not regarding the main contribution this is fine. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure the amount of images of a single identity used over TPR/FNR/FPR/TNR and accuracy with mean and standard deviation over 20 randomly sampled subset. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on idenity based adversarial attacks.
