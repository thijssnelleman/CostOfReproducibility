## Scaling Rectified Flow Transformers for High-Resolution Image Synthesis
Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, Dustin Podell, Tim Dockhorn, Zion English, Robin Rombach
Keywords:
Award: Best Paper
ICML/2024/Proceedings/2438 - Scaling Rectified Flow Transformers for High-Resolution Image Synthesis.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors claim that the have made their results, code, and model weights publically available, but fail to provide a link (+4).  
Brief mathematical formulations are given for the considered methods but no implementation details about any of them are mentioned (+4).  
Some mentions of using existing models are made ("we (...) use an off-the-shelf, state-of-the-art vision-language model, CogVLM...").  
A figure of the model architecture is provided.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(1?/3)

Various datasets were used throughout the work, but no links are provided (+1).  
Imagenet is known to be publically avaliable; for the other datasets the authors make no comments on availability (+1). Datasets are named with citations but no further statistics (+1) or descriptions (+1) are given.  
In Appendix B.3 they give additional information about how they transformed Imagenet to make it applicable to this generative task, yet the exact method for how they added captions to ImageNet is missing (+1).  

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

Appendix B.3 mentions the batch size, optimizer, learning rate, and number of warmup steps, among a few more hyperparameters, but no overview table is given (+2).  
The authors do not elaborate on how they chose these values (+2).
They also repeatedly mention the importance of the scale parameter s, but do not always specify the reasoning behind the values they chose for it in their experiments (+1).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[7]

The authors use CLIP scores and FID, but do not give explanations for these metrics (+1).  
Table 3 then lists Perceptual Similarity, SSIM and PSNR without any mention of these in the text (+1).  
The authors are sometimes ambiguous about their experiment setups with regards to which configurations were explored for which experiment type (See: "we only show the two best-performing variants (...) for different hyperparameters") (+1).  
The experiment setup for "human preference" refers to some benchmark but completely omits how these human preference ratings were obtained. It appears in Appendix C.3 that these preferences come from some dataset? But the lack of explanation adds too much guesswork. (+2)  
The authors do not mention whether experiments were only run once or on some repetition strategy (+1).  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The paper explores a large variety of variants of information flow for diffusion models. Without any previous knowledge of these diffusion models, it is hard to understand the very brief mathematical formulations the authors provide in Sections 2 and 3. 
This paper is written in a way that assumes the reader is closely familiar with the state of the art in image diffusion, and it would require substantial further reading into the literature before this paper becomes accessible to the average reader.