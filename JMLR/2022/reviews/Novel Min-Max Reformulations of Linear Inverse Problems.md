
## Novel Min-Max Reformulations of Linear Inverse Problems
Mohammed Rayyan Sheriff, Debasish Chatterjee
Keywords: 
JMLR/2022/Proceedings/20707 - Novel Min-Max Reformulations of Linear Inverse Problems.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

Implementation not provided. They state they use mattlab in the experiments with imnoise to add gausian noise to each image.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use single images and add noise to them through gaussian nosie and specify the library this was done with and under what parameter values. In 2.4.2 the authors conduct experiments with the Quadratic Program and describe it,m 2.4.3 the dictionary learning problem. The code for these problems is not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The algorithms only take in a few parameters and the authors specify the values per experiment (such as step size and initailisation values/formulas) but not always how they are acquired (some theoretically). No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method on image denoising and report the resulting values of single images as PSNR metric. Some y-axes are unlabelled so its not straight away clear what is being measured.  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on min-max and linear inverse problems.
