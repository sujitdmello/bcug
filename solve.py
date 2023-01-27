# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
import urllib.request
a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(sol1, sol2))

# Download the content from https://bcug.com and display it on the console
url = "https://bcug.com"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
print(text)
