# Interfaz del TAD

from TAD import Cola

c=Cola()
c.agregar('Pedro')
c.agregar('Juan')
c.agregar('Claudia')
c.agregar('Diego')
c.agregar('Sofia')
c.agregar('Luisa')
c.agregar('Mario')

print(c.mostrar())

c.avanzar()
c.avanzar()
c.avanzar()

print(c.primero())
print(c.ultimo())
print(c.mostrar())

