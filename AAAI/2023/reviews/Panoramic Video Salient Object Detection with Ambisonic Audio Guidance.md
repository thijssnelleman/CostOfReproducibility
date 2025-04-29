
## Panoramic Video Salient Object Detection with Ambisonic Audio Guidance
Xiang Li, Haoyuan Cao, Shijie Zhao, Junlin Li, Li Zhang, Bhiksha Raj
Keywords: CV: Video Understanding & Activity Analysis, CV: Multi-modal Vision, CV: Object Detection & Categorization, CV: Segmentation
AAAI/2023/Proceedings/25227 - Panoramic Video Salient Object Detection with Ambisonic Audio Guidance.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not provide a source for their implementation. In their implementation details they state its done in PyTorch. The authors give visua lexamples on the problem and a pipeline overview, including more detailed (modular or process) diagrams. However, the absence of real implementation documentation is pushing the cost very high up.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use a benchmark data set and cite the source. A short description on it is provided with some key features of the meta data. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Details on key hyperparameters are given in the implementation details section. It is not specified how these were acquired. It is unclear if the set of hyperparameters given is complete.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors discuss the metrics they use without explanation, but do provide citations for more information. The tables seem to indicate single run results. The training details are provided, although the exact way of splitting the test set is still unclear especially with the implementation docs not present.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The task presented in the paper is quite complex and the data used requires good understanding of computer vision. The metrics are not easy to grasp and in general it is a complex method. This is unnecesarrily worsened however with the absence of the implementation documentation as they serve as a guiding example with the paper.
