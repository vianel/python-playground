innmbr = int(input("Number: "))
epsilon = 0.01
lower = 0.0
high = max(lower, innmbr)
out = (high + lower) / 2

print(f'pre start out {out} innmbr {innmbr} high {high}')
while abs(out**2 - innmbr) >= epsilon:
    print(f'out is {out} lower is {lower} high is {high} epsilon is {epsilon}')
    if out**2 < innmbr:
        lower = out
    else:
        high = out

    out = (high + lower) / 2

print(f'sqare root {out}')
