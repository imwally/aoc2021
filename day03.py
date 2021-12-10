from statistics import mode

fname = "input03.txt"

# Part 1
with open(fname) as f:
    lines = f.read().splitlines()

    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []

    for line in lines:
        line_list = list(line)
        a.append(line_list[0])
        b.append(line_list[1])
        c.append(line_list[2])
        d.append(line_list[3])
        e.append(line_list[4])
        f.append(line_list[5])
        g.append(line_list[6])
        h.append(line_list[7])
        i.append(line_list[8])
        j.append(line_list[9])
        k.append(line_list[10])
        l.append(line_list[11])

gamma = ""
gamma += mode(a)
gamma += mode(c)
gamma += mode(d)
gamma += mode(b)
gamma += mode(e)
gamma += mode(f)
gamma += mode(g)
gamma += mode(h)
gamma += mode(i)
gamma += mode(j)
gamma += mode(k)
gamma += mode(l)

bin_gamma = int(gamma, 2)
bin_epsilon = bin_gamma ^ 0b111111111111

print(f"Day 1: {bin_gamma*bin_epsilon}")