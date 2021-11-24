import numpy
import argparse
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('traj_file')
    args = parser.parse_args()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    dst = args.traj_file.strip('.txt') + '.pdf'
    file = open(args.traj_file)
    data = file.read()
    lines = data.replace(","," ").replace("\t"," ").split("\n")

    List = []
    xList = []
    yList = []
    for i in range(len(lines) - 2):
        line = lines[i]
        next = lines[i+1]
        t, x, y, z, a, b, c, d = line.split(' ')
        t_, x_, y_, z, a, b, c, d = next.split(' ')
        if t == t_:
            if len(xList) == 0:
                continue
            List.append((xList.copy(), yList.copy()))
            xList = []
            yList = []
            continue
        xList.append(float(x))
        yList.append(float(y))

    for xl, yl in List:
        ax.plot(xl, yl)

    plt.savefig(dst, format="pdf")











#
