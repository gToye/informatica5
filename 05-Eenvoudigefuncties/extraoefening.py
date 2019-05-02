x = float(input("wat is de luchttemperatuut?"))
y = float(input('wat is de windsnelheid?'))

a = 0.6215*x
b = 0.3965*x
c = (3.6*y)**0.16
print(13.12+a+((b-11.37)*c))