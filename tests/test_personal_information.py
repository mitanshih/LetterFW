
'''
Created on 2025-02-06 15:15:08

@author: MilkTea_shih
'''

#%%    Packages
import pathlib
import unittest
import sys

from unittest.mock import MagicMock, mock_open, patch

sys.path.append(pathlib.Path(__file__).parents[1].as_posix())
from src.personal_information import login_information, _get_login_information

#%%    Variable


#%%    Functions
class TestGetLoginInformation(unittest.TestCase):
    """Unit tests for the _get_login_information function."""

    @patch('pathlib.Path.is_file', return_value=True)
    @patch('builtins.open', new_callable=mock_open,
           read_data="username1\npassword1\n")
    def test_file_exists(self, mock_file: MagicMock, mock_is_file: MagicMock
                         ) -> None:
        """Test _get_login_information when the file exists."""
        result: login_information = _get_login_information("admin.txt")
        self.assertEqual(result.username, "username1")
        self.assertEqual(result.password, "password1")

    @patch('pathlib.Path.is_file', return_value=False)
    @patch('builtins.input', return_value='y')
    def test_file_not_exists_use_default(self, mock_input: MagicMock,
                                         mock_is_file: MagicMock,
                                         ) -> None:
        """
        Test _get_login_information when the file does not exist 
        and user chooses to use the default account. 
        The function should return default account credentials.
        """
        result: login_information = _get_login_information("nonexistent.txt")
        self.assertEqual(result.username, "admin")
        self.assertEqual(result.password, "admin")

    @patch('pathlib.Path.is_file', return_value=False)
    @patch('getpass.getpass', return_value="custom_pass")
    @patch('builtins.input', side_effect=['n', "custom_user"])
    def test_file_not_exists_custom_input(self, mock_input: MagicMock,
                                          mock_getpass: MagicMock,
                                          mock_is_file: MagicMock,
                                          ) -> None:
        """
        Test _get_login_information when the file does not exist 
        and user chooses not to use the default account. 
        The function should prompt for custom credentials.
        """
        result: login_information = _get_login_information("nonexistent.txt")
        self.assertEqual(result.username, "custom_user")
        self.assertEqual(result.password, "custom_pass")

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    unittest.main()

#%%
