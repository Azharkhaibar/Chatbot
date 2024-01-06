import random

R_MAKAN = "gw kgk makan ngotak lahh!"
R_CURHAT = "gw bukan tempat curhat, pleaseee!!"

def tidak_diketahui():
    respons = ["sederhanain cobaa",
               "...",
               "apaan maksudnya jawa?",
               "apaan tu?",
               "gw ga ngerti pleasee",
               "hah maksudnya?"][random.randrange(6)]
    return respons
