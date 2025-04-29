
## ClimSim: A large multi-scale dataset for hybrid physics-ML climate emulation
Sungduk Yu, Walter Hannah, Liran Peng, Jerry Lin, Mohamed Aziz Bhouri, Ritwik Gupta, Björn Lütjens, Justus C. Will, Gunnar Behrens, Julius Busecke, Nora Loose, Charles Stern, Tom Beucler, Bryce Harrop, Benjamin Hillman, Andrea Jenney, Savannah L. Ferretti, Nana Liu, Animashree Anandkumar, Noah Brenowitz, Veronika Eyring, Nicholas Geneva, Pierre Gentine, Stephan Mandt, Jaideep Pathak, Akshay Subramaniam, Carl Vondrick, Rose Yu, Laure Zanna, Tian Zheng, Ryan Abernathey, Fiaz Ahmed, David Bader, Pierre Baldi, Elizabeth Barnes, Christopher Bretherton, Peter Caldwell, Wayne Chuang, Yilun Han, YU HUANG, Fernando Iglesias-Suarez, Sanket Jantre, Karthik Kashinath, Marat Khairoutdinov, Thorsten Kurth, Nicholas Lutsko, Po-Lun Ma, Griffin Mooers, J. David Neelin, David Randall, Sara Shamekh, Mark Taylor, Nathan Urban, Janni Yuval, Guang Zhang, Mike Pritchard
Keywords: 
Award: Outstanding Datasets and Benchmarks Paper
NeurIPS/2023/Proceedings/3080 - ClimSim: A large multi-scale dataset for hybrid physics-ML climate emulation.pdf
Project URL: https://leap-stc.github.io/ClimSim/README.html

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation on their project website (https://github.com/leap-stc/ClimSim/tree/main). The documentation is very impressive.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors construct their own dataset and publish it online. The construction is defined in sec 3. They define properties, collection strategies and sources. Extended dataset statistics are available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate six baselines on their new dataset. The code for each is available in the implementation. Their architectures are discussed in 4.1. Their HPs are summarised in the implementation code files (not a seperate files but still accesible). The authors state the HP optimisation for the MLP with the number of trials but not the strategy. In the supplementary materials the authors state the search domains for most hyperparameters. There they do state the strategy of optimisation per model and the budgets.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors define dataset splits in sec 3. The authors use MAE and R^2 and explain them in 4.3. In fig 2 they show the results where variance is 5-95 percentile. Aggregation and population not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise in climate emulation data. 
