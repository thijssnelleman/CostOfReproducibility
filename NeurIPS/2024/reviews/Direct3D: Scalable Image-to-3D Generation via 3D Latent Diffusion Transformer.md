
## Direct3D: Scalable Image-to-3D Generation via 3D Latent Diffusion Transformer
Wu Shuang, Youtian Lin, Yifei Zeng, Feihu Zhang, Jingxi Xu, Philip Torr, Xun Cao, Yao Yao
Keywords: 
NeurIPS/2024/Proceedings/93214 - Direct3D: Scalable Image-to-3D Generation via 3D Latent Diffusion Transformer.pdf
Project URL: https://www.neural4d.com/research/direct3d

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on their project page (https://github.com/DreamTechAI/Direct3D/). In the readme they state installation instructions, how to use the code, acknowledgements regarding other repos used for development. The code has few comments for some files. The structure is overseeable. Overview of the framework is in figure 2 and architecture in figure 3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use a filtered subset of the objaverse data set which they cite and a link is available in the repository. How this subset was created is not clear. Descriptions and statistics are minor. The authors use the Google Scanned Object GSO (Citation) for qualitative results and testing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors summarise their parameter values and architecture in 4.2. A structured overview of these values is missing. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics used for table 1 are camfer distance, IoU and F score (all standard), results are single model/run. The authors train on one data set and evaluate on 30 random sampels from the GSO dataset. Results are single run. The authors also do a user study to evaluate the method where the metrics is a score from 1-5 for which the authors state they asked 46 volunteers (pop size) to rate from 1-5 the quality of the output and what data was presented to the users.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on 3D CV and diffusion transformers.
