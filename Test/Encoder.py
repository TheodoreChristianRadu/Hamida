from math import isqrt

input = open('Input.txt', 'r')
output = open('Output.txt', 'w')
for line in input:
    for character in line:
        n = ord(character)
        d = isqrt(n)
        q, r = divmod(n, d)
        output.write(f">{d*'+'}[<{q*'+'}>-]<{r*'+'}.>\n")
