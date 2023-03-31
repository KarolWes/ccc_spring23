
# P=0, R=1, S=2;

def compare (A, B):
    if A == B:
        return A
    if A == 'P' and B == 'R':
        return 'P'
    if A == 'P' and B == 'S':
        return 'S'
    if A == 'R' and B == 'S':
        return 'R'

def task1(filename):
    f = open(filename, "r")
    f_out = open(filename.split('.')[0]+".out", "w")
    n = int(f.readline())
    for _ in range(n):
        style = f.readline()
        a = min(style[0], style[1])
        b = max(style[0], style[1])
        f_out.write(compare(a,b) + '\n')
    f.close()
    f_out.close()

if __name__ == '__main__':
    task1("data/level1_example.in")
    task1("data/level1_1.in")
    task1("data/level1_2.in")
    task1("data/level1_3.in")
    task1("data/level1_4.in")
    task1("data/level1_5.in")
