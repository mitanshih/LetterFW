
'''
Created on 2025-01-16 18:08:00

@author: MilkTea_shih

verify the legitimacy of email address
'''

#%%    Packages
import re

#%%    Variable
#[zh-TW can be the email address]: https://xn--fiq228c.tw/domain_name04.html
_pattern: re.Pattern = re.compile("".join((
    #[ref.]: https://support.google.com/mail/answer/9211434
    #"(",               #use to control the length of range for username
    "^\w+",             # Username starts with a letter, number or `zh-TW`.
    "((\.\w+)",         #can include '.'
    "|(\+\w+)",         #can include '+'
    #"|(\_\w+)",
    #"|(\-\w+)",
    #"|(\-\w+)",    #instead '-' to add the other symbols
    ")*",               #include as many repetitions as possible
    #"){6,30}",         #length of range for username
    "@",                #split *username* and *domain*
    "\w+",              # Domain starts with a letter or number for *tag*.
    "((\.|\-)\w+)*",    #can include '.' or '-' for many repetitions in *tags*
    "\.\w{2,63}$"       # Top-level domain is 2 to 63 word characters.
)))


#%%    Functions
def is_valid_email_address(address: str) -> bool:
    return False if _pattern.fullmatch(address) is None else True

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
