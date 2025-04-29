
## Euler-Lagrange Analysis of Generative Adversarial Networks
Siddarth Asokan, Chandra Sekhar Seelamantula
Keywords: 
JMLR/2023/Proceedings/201390 - Euler-Lagrange Analysis of Generative Adversarial Networks.pdf
Project URL: https://github.com/DarthSid95/ELF_GANs

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website (https://github.com/DarthSid95/ELF_GANs). In the readme they state installation instructions for two set ups, details on the implementation with examples, details on datasets and how to get data, how to run training commands with extensive examples. Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors conduct experiments on image datasets in 6.2 and use MNIST, SVHN, CelebA, CIFAR-10 and Ukiyo-E faces. Citations provided for all and download links in the implementation. Description/statistics lacking. They also conduct experiments on synthetic data described in 3.7. but code cannot be found.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state hyperparameters in algorithm 1 (batch size, learning rate, ..) and values stated for all experiments in 3.7. No acquisition specified. Structured overview missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors describe the metrics in 6.2: FID, RE, contuity of latent space (described, visually represented only) and sharpness of the image (described and citation given). Further more they use generator loss in figure 7. Results are single run. Data split unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on GAN and fourier-series.
