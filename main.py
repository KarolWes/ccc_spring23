import math


# P=0, R=1, S=2;
styles = {'S':0, 'L':1, 'P':2, 'Y':3, 'R':4}
def compare (A, B):
    if A == B:
        return A
    if A == 'P' and B == 'R':
        return 'P'
    if A == 'P' and B == 'S':
        return 'S'
    if A == 'R' and B == 'S':
        return 'R'

def big_compare(A,B):
    if A == B:
        return A
    elif A == 'P' and (B == 'Y' or B == 'R'):
        return 'P'
    elif A == 'Y' and (B == 'R' or B == 'S'):
        return 'Y'
    elif A == 'R' and (B == 'S' or B == 'L'):
        return 'R'
    elif A == 'S' and (B == 'L' or B == 'P'):
        return 'S'
    elif A == 'L' and (B == 'P' or B == 'Y'):
        return 'L'
    else:
        return big_compare(B,A)

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
    
def task4(filename):
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
        lowest = 2
        if dict['R'] > dict['P']:
            power = pl//2
            while power > 1:
                while dict['R'] >= power-1 and dict['P'] >= 1:
                    lowest = power
                    ans += 'P' + 'R'*(power-1)
                    dict['R']-= (power-1)
                    dict['P']-=1
                    # if dict['R'] <= dict['P']:
                    #     break
                power = power //2

            while dict['R'] > dict['P'] and lowest > 0:
                if dict['R'] >= lowest:
                    tmp = 'R' * lowest
                    dict['R'] -= lowest
                else:
                    tmp = 'R' *dict['R']
                    dict['R'] = 0
                while float(int(math.log(len(tmp), 2))) != math.log(len(tmp), 2) or len(tmp) < 2:
                    tmp += 'S'
                    dict['S'] -=1
                ans += tmp
                lowest = lowest // 2
            ans = gen_pairs(dict, ans)
        else:
            ans = gen_pairs(dict, ans)
        f_out.write(ans + "\n")

        styles = list(ans)
        players = len(styles)
        entries = styles
        results = []
        while players > 1:
            for i in range(0, players, 2):
                a = min(entries[i], entries[i + 1])
                b = max(entries[i], entries[i + 1])
                results.append(compare(a, b))
            players = players // 2
            entries = results
            results = []
        # print("".join(x for x in entries))
        if entries[0] != 'S':
            print(f"{filename} {k}")
    f.close()
    f_out.close()

def task5(filename):
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
        lowest = 2
        if dict['R'] > dict['P']:
            power = pl // 2
            while power > 1:
                while dict['R'] >= power - 1 and dict['P'] >= 1:
                    lowest = power
                    ans += 'P' + 'R' * (power - 1)
                    dict['R'] -= (power - 1)
                    dict['P'] -= 1
                    # if dict['R'] <= dict['P']:
                    #     break
                power = power // 2

            while dict['R'] > dict['P'] and lowest > 0:
                if dict['R'] >= lowest:
                    tmp = 'R' * lowest
                    dict['R'] -= lowest
                else:
                    tmp = 'R' * dict['R']
                    dict['R'] = 0
                while float(int(math.log(len(tmp), 2))) != math.log(len(tmp), 2) or len(tmp) < 2:
                    tmp += 'S'
                    dict['S'] -= 1
                ans += tmp
                lowest = lowest // 2
            ans = gen_pairs(dict, ans)
        else:
            ans = gen_pairs(dict, ans)
        f_out.write(ans + "\n")

        styles = list(ans)
        players = len(styles)
        entries = styles
        results = []
        while players > 1:
            for i in range(0, players, 2):
                a = min(entries[i], entries[i + 1])
                b = max(entries[i], entries[i + 1])
                results.append(compare(a, b))
            players = players // 2
            entries = results
            results = []
        # print("".join(x for x in entries))
        if entries[0] != 'S':
            print(f"{filename} {k}")
    f.close()
    f_out.close()

if __name__ == '__main__':
    #task5("data/level5_example.in")
    task5("data/level5_1.in")
    task5("data/level5_2.in")
    task5("data/level5_3.in")
    task5("data/level5_5.in")
    task5("data/level5_5.in")
    