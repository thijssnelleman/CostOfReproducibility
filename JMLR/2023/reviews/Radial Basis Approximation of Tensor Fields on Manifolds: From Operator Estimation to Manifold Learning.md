
## Radial Basis Approximation of Tensor Fields on Manifolds: From Operator Estimation to Manifold Learning
John Harlim, Shixiao Willing Jiang, John Wilson Peoples
Keywords: 
JMLR/2023/Proceedings/221193 - Radial Basis Approximation of Tensor Fields on Manifolds: From Operator Estimation to Manifold Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

Implementation not given. There is a link to some matlab code in the references but unclear if this is used. The authors state they use MATLAB in their experiments and a built-in kernal density estimation function.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(6/6)

The auhtors use simulated data and state their formulae in 5.2, 5.3 and 5.4 with parameters + values, but no implementations given.  

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors specify value of K in 5.2 and for some results the value of s is defined. In appendix E they demonstrate different values of K, epsilon. Its not very clear what the authors consider as parameters for each experiment and how the values are selected (Sometimes a grid, sometimes 'empirical' is stated, sometimes nothing at all) or what the selected values are for each experiment. It will take quite some effort to extract the information from the paper and fill in the gaps / defend against the gaps.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors calculate eigenvalues and measure error on it as well as 'spectra' / error on 'spectra
. Data split not applicable. Each experiments has 16 independent trials presented with the average but the variation is unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requries expertise on linear algebra.
