# Source: Understanding Computer Applications with BlueJ - X
# Evaluating expressions


# Expression to evaluate: P = a2 + bc

a =2.0
b =3.0
c =4.0

p = a*a + b*c 

print "Expression result: " + str(p)

# Expression to evaluate: m = (a^2 - b^2) / (ab)

m = (a*a - b*b) / (a*b)

print "Expression result: " + str(m)


# Expression to evaluate: s =  ut + 1/2 (a * t^2)

u =4.0
t =5.0

s = u * t + 0.5 * (a * t * t)

print "Expression result: " + str(s)

# Expression to evaluate: f =  uv / (u + v)

v =7.0

f = u * v / (u + v)

print "Expression result: " + str(f)

# Expression to evaluate: x =  (b^2 - 4ac) / 2a

x = (b*b - 4*a*c) / (2*a)

print "Expression result: " + str(x)

# Expression to evaluate: y =  2(lb + bh + lh)

l =4.0
b =5.0
h =6.0 

y = 2 * (l*b + b*h + l*h)

print "Expression result: " + str(y)

# Expression to evaluate: d =  a^2 + b^2

d = a*a + b*b

print "Expression result: " + str(d)

# Expression to evaluate: z =  x^3 + y^3 - xy 

x =4
y =5

z = x*x*x + y*y*y - (x*y)

print "Expression result: " + str(z)
