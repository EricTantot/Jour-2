positions = [ 
    ('Bob',  0.0, 21.0), 
    ('Cat',  2.5, 13.1), 
    ('Dog', 33.0,  1.2) 
]

out = []

for i in positions:
    out.append(i)

x = min(out)
y = max(out)

print(x,y)
