
## Optimized Crystallographic Graph Generation for Material Science
Astrid Klipfel, Yaël Frégier, Adlane Sayede, Zied Bouraoui
Keywords: Multidisciplinary Topics and Applications: MDA: Energy, environment and sustainability, Multidisciplinary Topics and Applications: MDA: Life sciences, Multidisciplinary Topics and Applications: MDA: Physical sciences, Machine Learning: ML: Feature extraction, selection and dimensionality reduction
IJCAI/2023/Proceedings/0836 - Optimized Crystallographic Graph Generation for Material Science.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/aklipf/mat-graph). In the readme they state a demo on how to use their code, installation requirements, and how to install. The code base is compact but basically has almost no comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors state data generation algorithm in algorithm 1. Code on this is available in the implementation. They perform this on data sets stated in section 3 where they describe them briefly with some statistics and citations. They are not linked.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method is parameter free, based on the algorithms/pseudo code presented. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate their method on the selected data sets for time (section 3) and other ocmputational efficiency metrics for various knn values.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires some base understanding of the problem and KNN.
