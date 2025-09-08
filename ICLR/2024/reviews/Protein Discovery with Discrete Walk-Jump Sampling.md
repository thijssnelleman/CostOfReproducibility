## Protein Discovery with Discrete Walk-Jump Sampling
Nathan Frey, Dan Berenberg, Karina Zadorozhny, Joseph Kleinhenz, Julien Lafrance-Vanasse, Isidro Hotzel, Yan Wu, Stephen Ra, Richard Bonneau, Kyunghyun Cho, Andreas Loukas, Vladimir Gligorijevic, Saeed Saremi
Keywords: 
Award: Outstanding Paper Award
ICLR/2024/Proceedings/2162 - Protein Discovery with Discrete Walk-Jump Sampling.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 4 of section 4.3 (https://github.com/prescient-design/walk-jump). The repo has an automated installation script provided. A small overview is given, where to find configs, how to use which parts of the code. Code has good comments. Structure is very large and needs a better index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

hu4D5 antibody dataset, cited, present in implementation. Description given, statistics lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

Appeneix A.5. and A.6. are dedicated to HP alpha, having a complete standalone analysis. The repository contains many configuration files to use, atlhough its not directly clear what belongs to where.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure in vitro success rate, distributional conformity score (explained and cited), as well as various subfield/task specific metrics. The authors present results on validation split, but not how this is done.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
