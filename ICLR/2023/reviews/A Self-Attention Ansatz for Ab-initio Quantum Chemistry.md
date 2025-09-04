## A Self-Attention Ansatz for Ab-initio Quantum Chemistry
Ingrid von Glehn, James Spencer, David Pfau
Keywords: 
ICLR/2023/Proceedings/11151 - A Self-Attention Ansatz for Ab-initio Quantum Chemistry.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the reproducibility statement (https://github.com/google-deepmind/ferminet). In the readme they state how to install, including instructions for GPU, how to test that the code works correctly, how to run the code with extensive examples, descriptions on the method, where the output can be found and a link to a notebook on how to analyse the output data. The code has great comments. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use various molecules as data, which they include in their implementation. The task is well explained throughout the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors refer for the majority of the HP values to the original work they build upon in section 4 with a few caveats. The values are summarised in appendix A.2.4 and in table 4/5. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure metrics specific to the task/subfield (energies). Results are single runs. Split does not apply.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
