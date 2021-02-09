import urllib.request as req

path = "./DATA/"
savefile = path + "mushroom.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, savefile)
print("download OK")