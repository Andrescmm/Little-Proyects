#Password Generator Andres Cusirramos 

#Import modules 
import random
from random import randint
import secrets
import string
import subprocess
import clipboard

def full_password(length):
    
    source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(secrets.choice(source)for i in range(length))
    return password

def nonSS_password(length):
    
    source = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = "".join(secrets.choice(source)for i in range(length))
    print("Password:", password)


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

data = full_password(20)
print (data)

copy2clip(data)

nonSS_password(20)
