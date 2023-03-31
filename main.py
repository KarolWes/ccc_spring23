
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
    n, pl = tuple(map(int, f.readline().split(' ')))


    for _ in range(n):
        styles = list(f.readline().strip())
        players = len(styles)
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

def gen_pairs(dict, ans):
    while dict['R'] > 0:
        ans += "RP"
        dict['R'] -= 1
        dict['P'] -= 1
    while dict['P'] > 0:
        if dict['S'] > 0:
            ans += "PS"
            dict['P'] -= 1
            dict['S'] -= 1
        else:
            ans += 'PP'
            dict['P'] -= 2
    while dict['S'] > 0:
        ans += 'SS'
        dict['S'] -= 2
    return ans
def task3(filename):
    f = open(filename, "r")
    f_out = open(filename.split('.')[0] + ".out", "w")
    n, pl = tuple(map(int, f.readline().split(' ')))
    for k in range(n):
        line = list(f.readline().strip().split(' '))
        dict = {}
        for entry in line:
            type = entry[-1]
            count = int(entry[:-1])
            dict[type] = count
        ans = ""
        if dict['R'] > dict['P']:
            while dict['R'] > dict['P']:
                if dict['R'] >= 3:
                    ans += 'RRRP'
                    dict['R']-=3
                    dict['P'] -=1
                else:
                    ans += 'RPRS'
                    dict['R'] -=2
                    dict['P'] -=1
                    dict['S'] -=1
            ans = gen_pairs(dict, ans)
        else:
            ans = gen_pairs(dict, ans)
        f_out.write(ans+"\n")

        styles = list(ans)
        players = len(styles)
        rounds = 2
        entries = styles
        results = []
        for _ in range(rounds):
            for i in range(0, players, 2):
                a = min(entries[i], entries[i + 1])
                b = max(entries[i], entries[i + 1])
                results.append(compare(a, b))
            players = players // 2
            entries = results
            results = []
        #print("".join(x for x in entries))
        if 'R' in entries:
            print(f'Error R {filename}, {k}')
        if 'S' not in entries:
            print('Error missing S')
    f.close()
    f_out.close()

if __name__ == '__main__':
    task3("data/level3_example.in")
    task3("data/level3_1.in")
    task3("data/level3_2.in")
    task3("data/level3_3.in")
    task3("data/level3_4.in")
    task3("data/level3_5.in")
    task2("data/level2_1.in")
    task2("data/level2_2.in")
    task2("data/level2_3.in")
    task2("data/level2_4.in")
    task2("data/level2_5.in")