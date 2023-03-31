
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

def task2(filename):
    f = open(filename, "r")
    f_out = open(filename.split('.')[0] + ".out", "w")
    results = []
    n, pl = tuple(map(int, f.readline().split(' ')))


    for _ in range(n):
        players = pl
        styles = list(f.readline().strip())
        rounds = 2
        entries = styles
        results = []
        for _ in range(rounds):
            for i in range(0, players, 2):
                a = min(entries[i], entries[i+1])
                b = max(entries[i], entries[i+1])
                results.append(compare(a,b))
            players = players//2
            entries = results
            results = []
        f_out.write("".join(x for x in entries) + '\n')


    f.close()
    f_out.close()

if __name__ == '__main__':
    task2("data/level2_example.in")
    task2("data/level2_1.in")
    task2("data/level2_2.in")
    task2("data/level2_3.in")
    task2("data/level2_4.in")
    task2("data/level2_5.in")