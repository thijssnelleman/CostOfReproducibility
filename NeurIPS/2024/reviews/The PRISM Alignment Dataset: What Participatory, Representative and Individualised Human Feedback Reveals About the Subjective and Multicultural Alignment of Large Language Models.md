
## The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models
Hannah Rose Kirk, Alexander Whitefield, Paul Rottger, Andrew M. Bean, Katerina Margatina, Rafael Mosquera-Gomez, Juan Ciro, Max Bartolo, Adina Williams, He He, Bertie Vidgen, Scott Hale
Keywords: 
Award: Datasets and Benchmarks Best Paper
NeurIPS/2024/Proceedings/923 - The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/HannahKirk/prism-alignment). In the readme they describe the work, the released data, details on what code can be found where, how to install. The code comes with a documentation website but this is not very information rich. The notebooks are very well documented. The repository structure is huge and can use an index. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors release a new data set, which they publish in their implementation and is described in great details throughout the entire paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors method itself is HP free but they do evaluate other methods on their data. In appenidx R.1 the authors briefly discuss these regarding clustering. No acquisition applicable.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors do not train any models but evaluated them. They use TF-IDF (stndard) and over-representation (formula given) and pairwise rank centrality as metrics. The results are over 100 randomly drawn participants over 1000 bootstraps and 6669 balanced conversations. aggregation is boxplots. In figure 5 they present violin plots with sample sizes given per violin.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP and dataset constructions and analysis.
