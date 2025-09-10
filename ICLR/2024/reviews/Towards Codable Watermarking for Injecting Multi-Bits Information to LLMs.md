## Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs
Lean Wang, Wenkai Yang, Deli Chen, Hao Zhou, Yankai Lin, Fandong Meng, Jie Zhou, Xu Sun
Keywords: 
ICLR/2024/Proceedings/18937 - Towards Codable Watermarking for Injecting Multi-Bits Information to LLMs.pdf
Project URL: https://openreview.net/attachment?id=JYu5Flqm9D&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors link their implementation in the abstract (https://github.com/lancopku/codable-watermarking-for-llm). The readme states details and download link on a dataset, details on models run, a note on a demo notebook and a few unstructured examples. There is a requirements file for installation purposes. The code has few comments. The structure is massive and has no index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

C4, cited and link in implementation. No description etc.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HPs detailed in text in appendix G. Structured overview missing, no motivation for all. It will take effort to determine the exact values per experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure success rate over perplexity over a range of parameter values. Data split not applicable. Single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
