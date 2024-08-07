from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return 'Nombre: {} '.format(self.nombre)

class articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'EL nombre es: {} la sección es {} y el precio es {}'.format(self.nombre,self.seccion,self.precio)

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


#the password of the superuser is jaam312