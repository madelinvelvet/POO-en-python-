class instrumento:
    def _init_(self, nombre, formageo, material):
        self.nombre = nombre
        self.formageo = formageo
        self.material = material
    def uso(self):
        print("Se utiliza en un laboratorio de química")
instrumento1 = instrumento()
instrumento1.nombre = "Beaker"
instrumento1.formageo = "Cilíndrica"
instrumento1.material = "Vidrio de borosilicato"
print(instrumento1.nombre)
print(instrumento1.formageo)
print(instrumento1.material)
instrumento1.uso()
instrumento2 = instrumento()
instrumento2.nombre = "Balanza"
instrumento2.formageo = "Indefinida"
instrumento2.material = "Metal y vidrio"
print(instrumento2.nombre)
print(instrumento2.formageo)
print(instrumento2.material)
instrumento2.uso()