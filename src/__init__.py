
'''
Created on 2025-01-19 01:31:32

@author: MilkTea_shih
'''

#%%    Packages
import sys

from pathlib import Path

#%%    Variable
# Get all Python files in the current directory of this file.
files = Path(__file__).parent.glob('*.py')

# Append the module names to `__all__` except __init__.py.
__all__ = [f.stem for f in files if f.is_file() and f.name != '__init__.py']

# Add 'src' folder to sys.path that Python can find the modules.
script_path: str = (Path(__file__).resolve().parents[1] / "src").as_posix()
if script_path not in sys.path:
    sys.path.append(script_path)

    # Using insert(0, path) to make sure the path has the highest priority.
    #sys.path.insert(0, script_path)
