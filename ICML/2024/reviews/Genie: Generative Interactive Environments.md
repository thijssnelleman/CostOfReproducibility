
## Genie: Generative Interactive Environments
Jake Bruce, Michael Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar, Richie Steigerwald, Chris Apps, Yusuf Aytar, Sarah Bechtle, Feryal Behbahani, Stephanie Chan, Nicolas Heess, Lucy Gonzalez, Simon Osindero, Sherjil Ozair, Scott Reed, Jingwei Zhang, Konrad Zolna, Jeff Clune, Nando de Freitas, Satinder Singh, Tim Rocktäschel
Keywords:
Award: Best Paper
ICML/2024/Proceedings/2270 - Genie: Generative Interactive Environments.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not share their implementation. They state in the acknowledgements what ecosystem they used for development. They provide some architecture overview in figure 4 and 5, and a very high level overview in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/2)

The authors state the model is trained 'from a large dataset of over 200,000 hours of publicly available internet gaming videos', called Platformers. This data is not text annotated. In the appendix the acquisition strategy is specified with some meta data on the resulting videos. The second dataset is provided with citation, is publicly available and has a short description but no direct link or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors specify various training details in appendix C. They are quite extensive, and the architecture details continue in appendix D. No acquisition strategy specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use two metrics (FVD and PSNR), which they explain in section 3. There is a mention of train/test split but it is not specified in the paper. The results are single models. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires a lot of practical experience with Gen AI for video games, as there is a lot of practical work to be done to collect this data and train these models on this kind of scale (11 billion parameters). The expertise required theoretically is actually 'overseeable'.
