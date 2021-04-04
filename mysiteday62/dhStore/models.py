from django.db import models

# Create your models here.
#   商店页面
# class category(models.Model):
#     cid = models.AutoField(primary_key=True)
#     cname = models.CharField(max_length=16, null=False, unique=True)
#     # password = models.CharField(max_length=16, null=False, unique=True)
#     # birthday = models.CharField(max_length=16, null=False, unique=True)
#     # email = models.CharField(max_length=16, null=False, unique=True)
#     # sex = models.CharField(max_length=16, null=False, unique=True)

# class orderitem(models.Model):
#     itemid = models.AutoField(primary_key=True)
#     count = models.CharField(max_length=32,null=False)
#     subtotal = models.CharField(max_length=16, null=False)
#     pid = models.CharField(max_length=32, null=False, unique=True)
#     oid = models.CharField(max_length=32, null=False, unique=True)

# class orders(models.Model):
#     oid = models.CharField(primary_key=True,max_length=32, null=False, unique=True)
#     orderitem = models.DateTimeField()
#     total = models.CharField(max_length=64, null=False)
#     state = models.CharField(max_length=64, null=False)
#     address = models.CharField(max_length=30, null=False)
#     name = models.CharField(max_length=20, null=False)
#     telephone = models.CharField(max_length=20, null=False)
#     uid = models.CharField(max_length=32, null=False)

# class product(models.Model):
#     pid = models.CharField(primary_key=True,max_length=32, null=False, unique=True)
#     pname = models.CharField(max_length=50)
#     market_price = models.CharField(max_length=50)
#     pimage = models.CharField(max_length=200)
#     pdate = models.DateField()
#     is_hot = models.CharField(max_length=11)
#     pdesc = models.CharField(max_length=255)
#     pflag = models.CharField(max_length=11)
#     cid = models.CharField(max_length=32)


# class user(models.Model):
#     uid = models.CharField(primary_key=True,max_length=32,null=False)
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     telephone = models.CharField(max_length=20)
#     birthday = models.DateField()
#     sex = models.CharField(max_length=10)
#     state = models.IntegerField()
#     code = models.CharField(max_length=64,null=True)
