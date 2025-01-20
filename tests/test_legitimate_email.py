
'''
Created on 2025-01-18 22:01:08

@author: MilkTea_shih

unittest for legitimate_email
'''

#%%    Packages
import pathlib
import unittest
import sys

sys.path.append(pathlib.Path(__file__).parents[1].as_posix())
from src.legitimate_email import is_valid_email_address

#%%    Variable
#[zh-TW can be the email address]: https://xn--fiq228c.tw/domain_name04.html

#%%    Functions
class TestLegitimateEmail(unittest.TestCase):
    valid_emails: tuple[str, ...]
    invalid_emails: tuple[str, ...]

    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_emails = (
            "test@example.com",
            "user.name+tag+sorting@example.com",
            "user.name@sub.domain.com",
            "x@x.co",
            "這.有@兩.個字"
        )
        cls.invalid_emails = (
            "missingdomain",
            "@missingusername.com",
            "comma@domain,com",
            "username@.com",
            "user@domain-.com",
            "user@onlytop-domain",
            "只有@壹.字"
        )

    def test_valid_email_address(self) -> None:
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email_address(email),
                                f"{email} should be valid")

    def test_invalid_email_address(self) -> None:
        for email in self.invalid_emails:
            with self.subTest(emails=email):
                self.assertFalse(is_valid_email_address(email),
                                 f"{email} should be invalid")


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    unittest.main(verbosity=1)  #default. 2 is detail log; 0 is only result.

#%%
