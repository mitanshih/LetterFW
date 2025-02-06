
'''
Created on 2025-01-14 16:29:19

@author: MilkTea_shih

get login information in private
'''

#%%    Packages
import dataclasses
import getpass
import pathlib

from log_logger import Logger

#%%    Variable
@dataclasses.dataclass
class login_information:
    username: str
    password: str

#%%    Functions
def _get_login_information(filepath: str = "admin.txt") -> login_information:
    """Get account information to access the database.

    Args:
        filename (str, optional): Filepath. Defaults to "admin.txt".

    Returns:
        login_information: The dataclass containing the username and password.
    """
    __logger: Logger = Logger()()

    __logger.info("Get login information.")
    content: list[str]    #database account information: [username, password]
    if pathlib.Path(filepath).is_file():
        with open(filepath, 'r') as f:
            content = f.readlines()

    else:
        __logger.warning(f'{filepath=} does not exist.')
        if input("To use default account?  (y/n): ").lower() == 'n':
            #NOTICE: pwinput.pwinput(prompt='PW: ', mask='X')
            # PW: XXXXXXXX -> input('PW: ') -> PW: password
            content = [input("Username: "), getpass.getpass("Password: ")]
        else:
            content = ['admin', 'admin']  #default account
            __logger.info(f"Use default account: {content}")

    return login_information(content[0].strip(), content[1].strip())

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    print(_get_login_information())

#%%
