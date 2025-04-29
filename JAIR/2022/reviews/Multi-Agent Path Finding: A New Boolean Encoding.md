
## Multi-Agent Path Finding: A New Boolean Encoding
Roberto Asín Achá, Rodrigo López, Sebastian Hagedorn, Jorge A. Baier
Keywords: 
JAIR/2022/Proceedings/13818 - Multi-Agent Path Finding: A New Boolean Encoding.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors publish their code online and state a link to it in footnote 2 of section 6.1 (https://github.com/robertoasin/MtMF). In the readme the authors state the input options with a description and what the output looks like. There are no compilation details, but there is a makefile. Code can use more comments. Structure is very large and can use an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors evaluate on benchmark instances from a previous work, cite it, describe them in 6.1. and give some statistics. No direct link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate their method with two different kinds of encoding. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure number of solved instances / percentage over running time with a time limit of 600 seconds and the final results summarised in table 2 and 3. They also present these over density degree (task specific).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires understanding of MA path finding and encoding.
