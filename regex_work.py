############Regex Work############
import re

text = 'include Ciphers aes128,aes192,aes256-ctr'
pattern = r'include Ciphers [a-zA-Z0-9,-]+'

match = re.search(pattern, text)
if match:
    extracted = match.group()
    print(extracted)

pattern = r'include Ciphers (?:aes(?:128|192|256-ctr),?)+'

pattern = r'include Ciphers aes128,aes192,aes256-ctr'


pattern = r'include\s+Ciphers\s+[a-zA-Z0-9,-]+'

texts = [
    "Some config include Ciphers aes128,aes192,aes256-ctr and other settings",
    "include Ciphers aes128,aes192,aes256-ctr",
    "The line says: include Ciphers aes128,aes192,aes256-ctr in the file"
]

pattern = r'include Ciphers [a-zA-Z0-9,-]+'

for text in texts:
    match = re.search(pattern, text)
    if match:
        print(f"Found: {match.group()}")
