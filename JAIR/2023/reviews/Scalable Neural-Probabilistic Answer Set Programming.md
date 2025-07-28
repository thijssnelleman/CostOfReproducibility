
## Scalable Neural-Probabilistic Answer Set Programming
Arseny Skryagin, Daniel Ochs, Devendra Singh Dhami, Kristian Kersting
Keywords: 
JAIR/2023/Proceedings/15027 - Scalable Neural-Probabilistic Answer Set Programming.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 1 (https://github.com/ml-research/SLASH). Overview in figure 2. In the readme they state installation notes, a quick note on the project structure, and how to get started. Code has pretty nice comments. Structure is fine.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use MNIST, Sudoku, VQAR, and set prediction task and provide citations on all. The authors also use ShapeWorld4 and CLEVR. Most have links provided in the implementation. Details are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the architectures in table 6, 8, 9, 10 and 11 and two HP values per method in table 7.  Acquisition not clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure recall over training data size, accuracy. There are quite a lot of different experiments going on, and a lot of notes are being made regarding training/testing sets but it will require the reader to have experience with a lot of different tasks/problems and emasurements.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on asnwer set programming.
