# Virtuelna mašina  



Za potrebe kursa je razvijena virtuelna mašina sa sledecim sadržajem:  

* Linux Mint 18.3  

* Python 3.6 + Anaconda 5.2.0  

* TensorFlow 1.9  

* Keras 2.2.2  

* OpenCV 3.4.1  

* Conda okruženje *soft* 



## Instalacija  



1. Instalirati <a href="https://www.virtualbox.org/">Oracle VM VirtualBox (5.2.x)</a>.

2. Preuzeti datoteku SoftComputingVM.zip sa sledeceg <a href="https://drive.google.com/drive/folders/1C2C1FmPI2fb1B_8gqGIfsazbN1Bag0_P?usp=sharing">linka</a>.  

3. Raspakovati datoteku SoftComputingVM.zip -> dobice se datoteka SoftComputingVM.vdi.
4. Otvoriti VirtualBox i napraviti novu VM: New -> Name: SoftComputingVM, Type: Linux, Version: Ubuntu (64-bit) -> Next.
5. Dodeliti bar 2GB (2048 MB) RAM za VM -> Next.
6. Izabrati Use an existing virtual hard disk file i sa diska odabrati datoteku SoftComputingVM.vdi -> Create.
7. Pokrenuti SoftComputingVM virtuelnu mašinu.


## Ako VM ne može da se pokrene
1. Unutar VirtualBox -> desni klik na SoftComputingVM -> Remove -> Remove only
2. Za svaki slucaj, pronaci gde se nalazi direktorijum VirtualBox VMs (u fajl sistemu) i ako u njemu postoji folder SoftComputingVM, obrisati samo taj folder.
3. Uraditi sve od 4. koraka u Instalacija virutelne mašine
 
Username na VM-u je "softcomputing”, a *sudo* lozinka je takode “softcomputing”.
