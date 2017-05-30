#!/usr/bin/env python
"""
MIT License
Copyright (c) 2017
Nicholas Purdy
nicholaswpurdy@gmail.com
github.com/NicholasPurdy/Simple-Secret-Sharing-Script
Written in python v2.7.6
"""
from __future__ import print_function
import sys
import os
import struct

def split_secret(f, num, name, odir):
    if not os.path.exists(odir):
        os.makedirs(odir)

    files, vals = list(), [i for i in range(0,num)]
    for i in range(0,num):
        of = open(odir + "/" + name + "_" + str(i), "w")
        files.append(of)

    byte = f.read(1)
    while byte != "":
        byte = ord(byte)

        for i in range(0, num-1):
            vals[i] = ord(os.urandom(1))
            files[i].write(struct.pack('B', vals[i])[0])
            byte = byte - vals[i]
        files[num-1].write(struct.pack('B', byte % 256)[0])
        byte = f.read(1)

def join_secret(path, shares, name):
    files = list()
    for sharefile in shares:
        f = open(path + "/" + sharefile, "r")
        files.append(f)

    out = open(name, "w")
    filesize, bytesread = os.path.getsize(path + "/" + shares[0]), 0
    while bytesread < filesize:
        byte = sum([struct.unpack('B', f.read(1))[0] for f in files])
        out.write(struct.pack('B', byte % 256)[0])
        bytesread = bytesread + 1


option = raw_input("Would you like to (S)plit a secret or (J)oin a secret? ")

if option == "S" or option == "s":
    print("\n--- New Secret ---\n")

    filename = raw_input("File of secret to split: ")
    f = open(filename, "r")
    num = raw_input("Number of shares to create (>1): ")
    name = raw_input("Share filename prefix: ")
    odir = raw_input("Name of output directory: ")
    split_secret(f, int(num), name, odir)

else:
    print("\n--- New Secret ---\n")

    path = raw_input("Directory name with shares: ")
    shares = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    name = raw_input("Filename to output to secret to: ")
    join_secret(path, shares, name)
