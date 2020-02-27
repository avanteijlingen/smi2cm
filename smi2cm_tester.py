import smi2cm

smi = "NC1=NCC(CCNC(=O)c2cc3c(cn2)[nH]c2ccccc23)N1"
cij = smi2cm.smi2cm(smi, 3, True)

smi2cm.visualise(smi)
