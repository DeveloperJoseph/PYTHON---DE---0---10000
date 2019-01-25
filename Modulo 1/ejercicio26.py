#PYTHON PIP #

#>What's Pip?
#Pip is a package manager Python packages, or modules if you like.
#Note: If you have Python version 3.4 or later, Pip is include by default.

#>What's a package?
#A package contains all the files you need for a module.
#Modules are Python code libraries  you can inclue in your project.

#>Check if Pip is Installed
#Navigate your command line to the location of Python's script directory, and 
#type the following: 'pip --version'

#>Download a Package
# Downloading a packe is very easy.
# Open the command line interface and tell PIP to download the package you want.
# Navigate your command line to the location of Python's script directory, and type
# the following.
#Example:
    # Download a packe named "camelcase". => pip install camelcase

# Now you have downloaded and installed your first package!   

# USING A PACKAGE: Once the package is installed, it is ready to use, also you can
# import the "camelcase" package into your project.
"""
import camelcase
c = camelcase.CamelCase()
tex="joseph sanchez smith"
print(c.hump(tex))
"""
# FIND PACKAGES: 
#Find more packages at https://pypi.org/
    
# REMOVE A PACKAGE: 
#Use the uninstall command to remove a package.
#Example: 
    # Uninstall the package named "camelcase" => pip uninstall camelcase

# LIST PACKAGES
# Uste the list command to list all the packages installed on your system.
# Example:
#           List installed packages => pip list

    