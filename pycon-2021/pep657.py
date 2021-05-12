x = {}
for i in range(50):
    x[i] = {}
    for j in range(12):
        x[i][j] = {j: i*j}
x[42][1][2] = None

# The following will raise an exception

print(x[42][1][2][3][4])
