# smi2cm
Generates and returns coulomb matrices from molecules encoded by SMILES strings.



Capable of threading to return lists of molecules



3D coordinates are found *via* the universal force field (UFF)



Adapted from: Rupp, M.; Tkatchenko, A.; Müller, K. R.; Von Lilienfeld, O. A. Fast and Accurate Modeling of Molecular Atomization Energies with Machine Learning. Phys. Rev. Lett. 2012, 108 (5), 1–5. https://doi.org/10.1103/PhysRevLett.108.058301.

Example (methanol):

36.8581052	34.32353208	5.40823835	5.39723812	5.39724143	3.11708716

34.3235321	73.51669472	3.90154962	3.87403015	3.87402937	8.06125494

5.40823835	3.90154962			 0.5			0.55381589	0.55381601	0.35023101

5.39723812	3.87403015	0.55381589				0.5		0.54992858	 0.43656715

5.39724143	3.87402937	0.55381601	0.54992858				0.5		0.43656714

3.11708716	8.06125494	0.35023101	0.43656715	0.43656714			0.5 



Usage:

```python
import smi2cm

smi = "c1cccc1" # benzene


#Get Coulomb matrix from 3D coordinates with hydrogens included

cij = smi2cm.smi2cm(smi, 3, Hs = True)


#Get Coulomb matrix from 2D coordinates with hydrogens excluded

cij = smi2cm.smi2cm(smi, 2, Hs = False)

```



Visualisation (depends: mayavi):

```python
import smi2cm

smi = "NC1=NCC(CCNC(=O)c2cc3c(cn2)[nH]c2ccccc23)N1" # tiruchanduramine

smi2cm.visualise(smi)
```



[![tiruchanduramine.png](https://i.postimg.cc/tTFdLj9m/tiruchanduramine.png)](https://postimg.cc/gXk6Z1Xv) molecule from: Ravinder, K.; Reddy, A. V.; Krishnaiah, P.; Ramesh, P.; Ramakrishna, S.; Laatsch, H.; Venkateswarlu, Y. Isolation and Synthesis of a Novel β-Carboline Guanidine Derivative Tiruchanduramine from the Indian Ascidian Synoicum Macroglossum. Tetrahedron Lett. 2005, 46 (33), 5475–5478. https://doi.org/https://doi.org/10.1016/j.tetlet.2005.06.060.

## Dependencies

Requires: NumPy, RDKit

Optional: mayavi (if you wish to use the visualise function)