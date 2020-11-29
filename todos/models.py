from django.db import models


class Departamento(models.Model):
    nombDepa = models.CharField(max_length=50)

    def __str__(self):
        return self.nombDepa

class Provincia(models.Model):
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    nombProvi = models.CharField(max_length=50)

    def __str__(self):
        return self.nombProvi

class Distrito(models.Model):
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    codProvi = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)
    nombDistri = models.CharField(max_length=50)

    def __str__(self):
        return self.nombDistri

class TipoInstitucion(models.Model):
    nombreTipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreTipo

class Institucion(models.Model):
    nombInsti = models.CharField(max_length=50)
    sigla = models.CharField(max_length=50)
    Representante = models.CharField(max_length=50)
    Domicilio = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Ruc = models.CharField(max_length=50)
    Situacion = models.CharField(max_length=50)
    codTipo = models.ForeignKey(TipoInstitucion, null=True, on_delete=models.CASCADE)
    codDepa = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE)
    codProvi = models.ForeignKey(Provincia, null=True, on_delete=models.CASCADE)
    codDistri = models.ForeignKey(Distrito, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombInsti