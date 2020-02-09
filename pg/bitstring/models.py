from django.db import models
import django_postgres
import psycopg2

class BloomFilter(models.Model):
    name = models.CharField(max_length=100)
    bitmap = django_postgres.BitStringField(max_length=8)


bloom = BloomFilter.objects.create(name='test')
print(bloom.bitmap)
bloom.save(force_update=True)


BloomFilter.objects.filter(bitmap='00100000')