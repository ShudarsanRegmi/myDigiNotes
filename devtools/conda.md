# **Conda Cheatsheet**  

#### **Basic Commands**
```bash
conda --version           # Check Conda version
conda update conda        # Update Conda
conda update anaconda     # Update Anaconda distribution
```

#### **Environment Management**
```bash
conda create -n myenv python=3.9  # Create environment with Python 3.9
conda env list                    # List all environments
conda info --envs                  # Another way to list environments
conda activate myenv               # Activate environment
conda deactivate                   # Deactivate environment
conda remove --name myenv --all     # Delete environment
```

#### **Package Management**
```bash
conda list                  # List installed packages
conda search numpy          # Search for package
conda install numpy         # Install package
conda install numpy=1.21    # Install specific version
conda update numpy          # Update package
conda remove numpy          # Uninstall package
```

#### **Installing from Channels**
```bash
conda install -c conda-forge numpy        # Install from Conda-Forge
conda config --add channels conda-forge   # Add Conda-Forge permanently
```

#### **Export & Import Environments**
```bash
conda env export > environment.yml    # Export environment
conda env create -f environment.yml   # Create environment from file
```

#### **Conda Virtual Environments with Pip**
```bash
conda install pip            # Install pip inside Conda environment
pip install somepackage      # Install package using pip
```

#### **Cloning & Managing Environments**
```bash
conda create --name myclone --clone myenv  # Clone an environment
conda list --explicit > spec-file.txt      # Save exact package list
conda create --name newenv --file spec-file.txt  # Recreate environment
```

#### **Clean Up**
```bash
conda clean --all   # Remove unused packages & cache
```

## For Windows

```bash
conda init powershell
```
OR
```bash
conda init cmd.exe
```

> These commands should be used to init conda environment. With the command, Conda modifies your PowerShell startup profile so that every time you open PowerShell, the conda environment is automatically set up and ready to use.

