# Problem statement
![](https://i.ibb.co/RzWkkmN/image.png)

Two-dimensional transition metal dichalcogenides (TMDCs) are relatively new types of materials that have remarkable properties ranging from semiconducting, metallic, magnetic, superconducting to optical. The chemical composition of TMDCs is MX₂; where M is the group of transition elements most popular Molybdenum and Tungsten, and X is usually Sulfur or Selenium. Atomically thin TMDCs usually contain various defects, which enrich the lattice structure and give rise to many intriguing properties. Engineered point defects in two-dimensional (2D) materials offer an attractive platform for solid-state devices that exploit tailored optoelectronic, quantum emission, and resistive properties. Naturally occurring defects are also unavoidably important contributors to material properties and performance. The immense variety and complexity of possible defects make it challenging to experimentally control, probe, or understand atomic-scale defect-property relationships. In the figure above you can find vacancy and substitution defects in an 8x8 MoS₂ crystal lattice.


Band gap is one of the important physical attributes which describe certain characteristics of the material, that helps deriving material qualities including electric conductivity or catalytic power or photo-optical properties. Band gap is the energy difference between the valence band and conduction band and is closely related to the energy difference between highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO), materials with overlapping (between valence band and conduction band) or very small band gap are conductors and materials with small bandgap are semiconductors while materials with large bandgap are insulators.

## Objective 
The task is to predict band gap energy for each crystal structure.

## Data
The training dataset is in the `data` directory in the baseline and structured into a directory called `structures` containing 2967 crystal structures as a json file named with a unique identifier and is containing a special pymatgen structure (check pymatgen documentation for [reference](https://pymatgen.org/index.html)), that contains information about crystal parameters, cartesian coordinates of each atom, atom types, and other information. The targets are stored in a csv file named targets.csv containing two columns; the first is the unique identifier of the structure and the other is the band gap value for each structure. The train and test sets are constructed by sampling the corresponding subset without replacement.

## Quality Metric
Energy within Threshold (EwT) is designed to measure the practical usefulness of a model for replacing [DFT](https://en.wikipedia.org/wiki/Discrete_Fourier_transform) by evaluating whether the predicted energy is close to the ground truth (DFT energy). EwT is defined as the fraction of structures in which the predicted energy is within ε = 0.02 eV ([electronvolt](https://en.wikipedia.org/wiki/Electronvolt)) of the ground truth energy. 

<img src="https://render.githubusercontent.com/render/math?math=\text{EwT} = \frac{1}{N}\sum_i \left| E_{\text{predicted},i} - E_{\text{DFT},i} \right| < \epsilon">

where <img src="https://render.githubusercontent.com/render/math?math=N"> is the number of samples in the dataset indexed by <img src="https://render.githubusercontent.com/render/math?math=i">.

## Baseline
The baseline is based on [MEGNet](https://arxiv.org/pdf/1812.05055.pdf), a message passing graph neural network designed for materials by incorporating the natural symmetries in crystals such as rotation invariance, and periodic boundary conditions (PBC). In the reference baseline MEGNet is trained on the dataset.

## Constraints
1. **Resource constraints**: The solution you submit will run with resource constraints of 1 CPU and 2 Gb RAM. The time limit is 15 minutes. Note that the running time on your machine and on Yandex.Contest servers could be different due to different hardware. 
1. DFT is not allowed; and, its use will disqualify the modeling solution from the competition

## Notes
You may use additional information, data, and advice at your own risk. All solutions will be checked by the jury to guarantee fair play. Please ask us in any vague or unclear case. If you face any problems or have questions, please contact us via e-mail: <a href = "mailto:hello@idao.world">hello@idao.world</a>

## References
* <a href="https://arxiv.org/pdf/1812.05055.pdf">Chen, C., Ye, W., Zuo, Y., Zheng, C. and Ong, S.P., 2019. Graph networks as a universal machine learning framework for molecules and crystals. Chemistry of Materials, 31(9), pp.3564-3572.</a>
* <a href="https://ir.nsfc.gov.cn//paperDownload/ZD5437990.pdf" target="_blank">Hu, Z., Wu, Z., Han, C., He, J., Ni, Z. and Chen, W., 2018. Two-dimensional transition metal dichalcogenides: interface and defect engineering. Chemical Society Reviews, 47(9), pp.3100-3128.</a>
* <a href="https://www.nature.com/articles/natrevmats201733" target="_blank">Manzeli, S., Ovchinnikov, D., Pasquier, D., Yazyev, O.V. and Kis, A., 2017. 2D transition metal dichalcogenides. Nature Reviews Materials, 2(8), pp.1-15.</a>
