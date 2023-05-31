import pygame
import pickle
from os import path

def store(item,file):
  with open(file,"wb") as f:
    pickle.dump(item,f)

def collect(file):
  if path.exists(file):
    with open(file,"rb") as f:
      return pickle.load(f)
  return None

FILE = "data.pkl"
data = collect(FILE)
if data is None:
  data = {}

# Edit data here
# https://replit.com/@RyanMagnus/Serialization#main.py

store(data, FILE)