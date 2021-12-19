import pandas as pd


def read_input():
    lines = []
    points = []
    with open('../inputs/input5.txt') as file:
        for line in file:
            lines.append(line.rstrip().lstrip())
    for line in lines:
        raw = line.split(" -> ")
        points.append(raw)
    return points

# rework this to actually solve 1, idk why i did my work over top of my already working solution for 1...
def solve1(input):
    points = []
    for line in input:
        start = line[0].split(",")
        end = line[1].split(",")
        if start[0] == end[0] or start[1] == end[1]:
            points.append(line)
        else:
            slope = abs((int(start[1]) - int(end[1])) / (int(start[0]) - int(end[0])))
            if slope == 1:
                points.append(line)
    overlaps = []
    line_points = []
    for line in points:
        start = line[0].split(",")
        end = line[1].split(",")
        if start[0] == end[0]:
            for y in range(abs(int(start[1]) - int(end[1])) + 1):
                point = [int(start[0]), min(int(start[1]), int(end[1]))+y]
                if point in line_points:
                    if point not in overlaps:
                        overlaps.append(point)
                else:
                    line_points.append(point)
        elif start[1] == end[1]:
            for x in range(abs(int(start[0]) - int(end[0])) + 1):
                point = [min(int(start[0]), int(end[0]))+x, int(start[1])]
                if point in line_points:
                    if point not in overlaps:
                        overlaps.append(point)
                else:
                    line_points.append(point)
    print(line_points)
    print(overlaps)
    print(len(overlaps))

def solve2(input):
    points = []
    for line in input:
        start = line[0].split(",")
        end = line[1].split(",")
        if start[0] == end[0] or start[1] == end[1]:
            points.append(line)
        else:
            slope = abs((int(start[1]) - int(end[1])) / (int(start[0]) - int(end[0])))
            if slope == 1:
                points.append(line)
    overlaps = []
    line_points = []
    for line in points:
        start = line[0].split(",")
        end = line[1].split(",")
        if start[0] == end[0]:
            for y in range(abs(int(start[1]) - int(end[1])) + 1):
                point = [int(start[0]), min(int(start[1]), int(end[1]))+y]
                if point in line_points:
                    if point not in overlaps:
                        overlaps.append(point)
                else:
                    line_points.append(point)
        elif start[1] == end[1]:
            for x in range(abs(int(start[0]) - int(end[0])) + 1):
                point = [min(int(start[0]), int(end[0]))+x, int(start[1])]
                if point in line_points:
                    if point not in overlaps:
                        overlaps.append(point)
                else:
                    line_points.append(point)
        else: # must be a diagonal
            x_delta = 1
            if int(start[0]) > int(end[0]): # if the starting x is to the right of the ending x
                x_delta = -1
            y_delta = 1
            if int(start[1]) > int(end[1]): # if the starting y is above the ending y
                y_delta = -1
            delta = 0
            while True:
                if delta > 1000:
                    print()
                point = [int(start[0]) + delta*x_delta, int(start[1]) + delta*y_delta]
                if point in line_points:
                    if point not in overlaps:
                        overlaps.append(point)
                else:
                    line_points.append(point)
                if int(start[0]) + delta*x_delta == int(end[0]) and int(start[1]) + delta*y_delta == int(end[1]):
                    break
                delta += 1
    print(line_points)
    print(overlaps)
    print(len(overlaps))

def main():
    input = read_input()
    solve1(input)
    solve2(input)

main()