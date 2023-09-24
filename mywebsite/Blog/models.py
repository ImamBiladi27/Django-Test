from django.db import models

# Create your models here.

class kategori(models.Model):
    id_kategori = models.IntegerField()
    nama_kategori = models.CharField(max_length=100)
    def __str__(self):
        return self.nama_kategori
class status(models.Model):
    id_status = models.IntegerField()
    nama_status = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_status

class produk(models.Model):
   
    id_produk = models.IntegerField()
    nama_produk = models.CharField(max_length=255)
    status_id = models.ForeignKey(status, on_delete=models.CASCADE)
    harga = models.IntegerField()
    kategori_id = models.ForeignKey(kategori,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.status_id