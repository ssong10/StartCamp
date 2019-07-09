# Create dummy files
import os
import random

family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['은정','인성','준영','태우','진희','태수','현택','지영','혜진','용흠','겨레','동환','경호','승열','지민','은비','지수','병준','선형','무연','성철','순범']

for i in range(500):
    cmd = f"touch ./dummy/{i+1}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)