import json
import matplotlib.pyplot as plt
import numpy as np
import os



# def plotraw():
#
#     with open('./learning/data//output.txt', "r") as infile:
#         mylist = json.load(infile)
#     #convert from list zu nparray
#     a = np.asarray(mylist)
#
#     plt.figure()
#     plt.ylabel('highest Value')
#     plt.xlabel('Episode')
#
#     plt.plot(a[:,0], a[:,1], 'r.-')
#     plt.show()

outputname = "test99"
path  = os.getcwd()

def plotmeans(mean_of_every_x_episodes):
    with open(path + '/data/'+outputname+'output.txt', "r") as infile:
      mylist = json.load(infile)

      #extract first item from list which is the configuration info
      configtext = mylist[0]
      mylist.pop(0)
      print(mylist)

      # convert from list zu nparray
    numplist = np.asarray(mylist)
    i=0
    current = np.array([0,0])

    while i < (len(numplist) / mean_of_every_x_episodes):
      new_value = np.mean(numplist[i*mean_of_every_x_episodes:(i+1)*mean_of_every_x_episodes], axis=0)
      current = np.vstack((current, new_value))
      #print(new_value)
      i = i + 1

    current = np.delete(current, 0, 0)
    #print(current)

    plt.figure()
    plt.plot(current[:, 0], current[:, 1], 'r.-')
    plt.title(configtext, fontsize=10)
    plt.ylabel('highest Value')
    plt.xlabel('Episode')
    plt.text(4, 1, configtext, ha='left', rotation=15, wrap=True)
    plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=200)
    plt.show()


plotmeans(1000)
