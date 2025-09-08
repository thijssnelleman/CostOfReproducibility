## Learning Interactive Real-World Simulators
Sherry Yang, Yilun Du, Seyed Ghasemipour, Jonathan Tompson, Leslie Kaelbling, Dale Schuurmans, Pieter Abbeel
Keywords: 
Award: Outstanding Paper Award
ICLR/2024/Proceedings/1065 - Learning Interactive Real-World Simulators.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors provide a link to a demo website, but no implementation. Figure 1/2 give a high level overview.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[8]

(11/14)

The authors list the datasets used in appendix B: Habitat HM3D, Language Table sim, Bridge Data, RT-1 data, Language Table real, Miscellaneous robot videos (unpublished), Ego4D, Something-Something V2, EPIC-KITCHENS, Miscellaneous human videos 50k (unpublished), Panorama scan Matterport Room-to-Room scans, Internet text-image LAION-400M, ALIGN, Internet video Miscellaneous videos (Unpublished). All except the unpublished datasets are cited. But the unpublished datasets have zero information on them and all datasets were used for training and part of the tvt split, thus making the impact higher (It is more difficult to take one or more of the public datasets and argue that the results are the same or how they differ from theirs.)

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values summarised in appendix C, table 6. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors specify the static splits per experiment, measuring FID ↓ FVD ↓ IS ↑ CLIP ↑ (not explained), results are single models.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[8]

-
