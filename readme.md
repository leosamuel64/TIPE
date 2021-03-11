# TIPE - MP 2020-2021

## Installer WSL1

### Activer la fonctionnalité "sous systeme Windows pour Linux"

- Aller dans "Panneau de configuration" > "Programmes" > "Activer ou désactiver des fonctionnalités Windows"
- Cocher la case : "Sous-système Windows pour linux"

### Installer WSL1

- Ouvrir le PowerShell (Windows+R -> powershell)

- Exécuter :
```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- Redémarrer votre ordinateur

### Installer une distribution Linux

- Ouvrir le Microsoft Store
- Chercher "Debian"
- Installer Debian
- Ouvrir Debian

- Créer un nouveau compte en suivant les consignes du terminal

- Fermer le terminal

Pour ouvrir un nouveau terminal (Windows+R > bash)

### Installation des bases

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install make
sudo apt install cmake
sudo apt install git

sudo pip3 install opencv-python
```

## Installer et compiler MetabotAPI

```python
sudo git clone -b jupyter https://github.com/Rhoban/MetabotAPI
```

```python
cd python
mkdir build
cd build
cmake ..
make
```

## Clonner le repository TIPE

```
sudo git clone https://github.com/leosamuel64/TIPE
```

