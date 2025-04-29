
## Scaling Rectified Flow Transformers for High-Resolution Image Synthesis
Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, Dustin Podell, Tim Dockhorn, Zion English, Robin Rombach
Keywords:
Award: Best Paper
ICML/2024/Proceedings/2438 - Scaling Rectified Flow Transformers for High-Resolution Image Synthesis.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors are 'considering making code publicly available'. Later they state they do this. No links can be found. An overview can be seen in figure 2. The authors link two repositories they used in their implementation. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/3)

The authors use two datasets for training and a third's validation set. All of these datasets are publicly available and citations are provided. The authors describe the data augmentation for their task in appendix B.3. Detailed descriptions, statistics and direct links are missing. The augmented version of the data is also not released, increasing the cost.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors details the hyperparameters used in appendix B.3. However, no overview is given on the hyperparameter space except for the list of values. The architecture is described in figure 2, however exact values/structure is not given. No acquisition specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors specify the training vs validation data in section 5.1 and appendix B.3. The authors use ranking, FID and CLIP scores as metrics and provide citations on them but do not explain them. They also state they only show the best performing variants but not exactly how this is presented. The authors state the averaging per experiment in table captions and the appendix B.3. The authors state they also report 'human preference' but not how this is acquired (human evaluation?).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requires expertise on diffusion models, CV (image generation) and a lot of practical experience as well as these are extremely large models.
