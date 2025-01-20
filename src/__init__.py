
'''
Created on 2025-01-19 01:31:32

@author: MilkTea_shih
'''

#%%    Packages
from pathlib import Path

#%%    Variable
# Get all Python files in the current directory of this file.
files = Path(__file__).parent.glob('*.py')

# Append the module names to `__all__` except __init__.py.
__all__ = [f.stem for f in files if f.is_file() and f.name != '__init__.py']
