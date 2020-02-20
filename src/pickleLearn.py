import pickle

with open("./testp.yml", "wb") as f:
    pickle.dump("{a:12}", f)

with open("./testp.yml", "r") as f:
