import numpy
import argparse
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('map_file')
    args = parser.parse_args()

    dst = args.map_file.strip('.txt') + '.pdf'
    file = open(args.map_file)
    data = file.read()
    lines = data.replace(","," ").replace("\t"," ").split("\n")
    xyzList = []
    for line in lines:
        if len(line) < 2: continue
        x, y, z = line.split(" ")
        xyzList.append([float(x), float(y), float(z)])
    xyzArray = numpy.array(xyzList)
    areaArray = numpy.ones(xyzArray.shape[0]) * 0.1

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(xyzArray[:,0], xyzArray[:,1], s=areaArray, marker=',', c=xyzArray[:,2])

    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    plt.axis('equal')
    plt.savefig(dst, format="pdf")











#
