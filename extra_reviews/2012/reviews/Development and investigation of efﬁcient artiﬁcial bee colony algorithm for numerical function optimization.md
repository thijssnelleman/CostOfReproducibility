## Development and investigation of efﬁcient artiﬁcial bee colony algorithm for numerical function optimization
Guoqiang Li, Peifeng Niu, Xingjun Xiao
Keywords: Artiﬁcial bee colony, Gbest-guided ABC, Biological-inspired optimization, Optimization
extra_reviews/2011/Proceedings/Development and investigation of efﬁcient artiﬁcial bee colony algorithm for numerical function optimization.pdf
$PROJECT URL$

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[6]

The authors provide a link to the implementation in the corrective appendix (http://zhihuiyuang.blog.163.com/blog/static/7893024920126258932615/), but this yields a 503 error. There is detailed pseudo code given in section 2 and 3. A detailed diagram is present in figure 1. Together they provide a substantial amount on the method for implementation, but no practical details such as frameworks or code provided.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use functions (synthetic data) as input problem. They are listed in table 2 with parameter values, and their solutions in table 3 with more details in table 4/5/6. Implementation not provided, but the authors cite the original work that introduced these functions and it is very well documented. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors list the parameters of their algorithm throughout the paper (mainly sec 3), but a structured overview is missing (Pseudo code has some structure, but a clear list of the parameters is not found there). Values are listed in text in section 5. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors repeat each experiment 30 times and report mean + std deviation. Datasplit not applicable. Each result states on which function the experiment was run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
