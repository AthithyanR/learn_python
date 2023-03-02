#!/usr/bin/env python3
from multiprocessing import Pool
import os

def sleepy(_):
    os.system("aria2c")

def start():
    with Pool(5) as p:
        p.map(sleepy, [None] * 5)

if __name__ == "__main__":
    start()