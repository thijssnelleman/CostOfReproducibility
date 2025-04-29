
## SinDDM: A Single Image Denoising Diffusion Model
Vladimir Kulikov, Shahar Yadin, Matan Kleiner, Tomer Michaeli
Keywords: 
ICML/2023/Proceedings/23700 - SinDDM: A Single Image Denoising Diffusion Model.pdf
Project URL: https://matankleiner.github.io/sinddm/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide pseudo code in algorithm 1 and 2. Oerview is available in figure 3 and 4. The authors provide a link to their project page where they post a link to their implementation (https://github.com/fallenshock/SinDDM). In the readme they state a table of contents, how to install the requirements, overview on the repository structure, extensive examples on how to use the training code and sample, and state where provided data can be found. They also acknowledge a source for implementation of the code. The code has an acceptable amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors include data in their implementation link. They are single images of diverse styles on which they train their method. Due to the small size and simplicity of the data set, this is a 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors share the appendix on their project page. In appendix C they state the configuration used for their method. An overview is also available in the main method of their implementation. N oacquisition method specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors report mean and standard deviation. They sample each training image 50 times. The metrics are pixel std and LPIPS dev which are not explained. Test set is not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with CV and diffusion models.
