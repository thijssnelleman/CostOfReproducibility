
## Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, Jonathan Ho, David Fleet, Mohammad Norouzi
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/734 - Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors provide extensive details on the implementation with pseudo code and figure in appendix F. They also link a library they used for their implementation (Which also specifies the framework JAX). The code is not released.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(3/4)

The authors use MS-COCO and DrawBench as datasets. MS-COCO has no details provided. The authors introduce DrawBench in this work, and describe it in sec 3 and appendix C. The dataset is available online. It is a fairly simple dataset (A prompt with a category). The authors also use a private datasets ("internal") and the LAION-400M dataset (Only citation provided). As the training private training dataset is used for each result, this has been weighted more heavily.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter as code in appendix F (and in text as well). The acquisition is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors compare single models. The authors conduct a user study (n = 25) and details the questions in appendix C.  Metrics are FID and proportionality of the user study. Variance is 95% confidencde but aggregation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on large Diffusion model with NLP (Text-to-image).
