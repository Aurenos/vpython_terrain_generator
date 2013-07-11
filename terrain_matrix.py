#-------------------------------------------------------------------------------
# Name:        Terrain Generator
#
# Author:      Kile Deal & Piero Barbagelata
#
# Created:     13/06/2012
#
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from visual import *
from random import randint, random

def print2D(array):
    for subset in array:
        for each in subset:
            print "%.2f\t" % each,
        print

def expand_horizontally(array):
    for subset in array:
        new_values = []
        subset_pos = array.index(subset)
        for i in range(len(subset)):
            new_values.append( (subset[i]+subset[i+1])/2.0 )
            if array[subset_pos].index(subset[i]) == array[subset_pos].index(subset[-2]): break
        k = 1
        for val in new_values:
            subset.insert(k,val)
            k += 2
    return array

def expand_vertically(array):
    new_lists = []
    for i in range(len(array)-1):
        new_list = []
        subset = i
        index = 0
        for j in array[subset]:
            try: # I was feeling lazy...
                down = array[subset+1][index]
            except IndexError:
                break
            avg = (j+down)/2.0
            new_list.append(avg)
            index += 1

        new_lists.append(new_list)
    k = 1
    for val in new_lists:
        array.insert(k, val)
        k += 2
    return array

def expand_matrix(array, amount=1):
    while amount > 0:
        array = expand_horizontally(array)
        array = expand_vertically(array)
        print len(array[0]),"x",
        print len(array)
        AddChaos(array)
        amount -= 1
    return array

def AddChaos(arr):
    for i in range(0,(len(arr)**2)/4):
        arr[randint(1,len(arr)-1)][randint(1,len(arr[0])-1)] = random()*10

def main():
    seeds = [[randint(10,150), randint(10,150), randint(10,150), randint(10,150)],
             [randint(10,150), randint(10,150), randint(10,150), randint(10,150)],
             [randint(10,150), randint(10,150), randint(10,150), randint(10,150)],
             [randint(10,150), randint(10,150), randint(10,150), randint(10,150)]]
    seeds = expand_matrix(seeds,7)
    #print2D(u)

    # Visual Stuff
    scene.height = 750
    scene.width = 750
    terrain_length = len(seeds[0])
    terrain_width = len(seeds)

    startx = -terrain_length/2.0
    startz = -terrain_width/2.0
    for i in range(terrain_width-1):
        #rate(20)
        for j in range(terrain_length-1):

            cylinder(pos=(startx,-25,startz), axis=(0,seeds[i][j]/2.0,0), radius=0.5,
            color=(float(seeds[i][j]/50),float(seeds[i][j]/25),float(seeds[i][j])/100))
            startz+=1
        startx+=1
        startz = -terrain_width/2.0

if __name__ == '__main__':
    main()
