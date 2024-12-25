from django.db import models

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    is_activate = models.BooleanField(default=False)
    image = models.ImageField(upload_to='person/',null=True,blank=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"{self.full_name}"
    




# class Direcror(models.Model):
#     name = models.CharField(max_length=200)

# class Production(models.Model):
#     name = models.CharField(max_length=250)

# class Cast(models.Model):
#     name  = models.TextField()

# class Tags(models.Model):
#     name = models.TextField()

# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     picture = models.ImageField(upload_to='person/',null=True,blank=True)
#     release_date = models.DateField()
#     duration = models.CharField(max_length=50)
#     rating = models.FloatField()
#     description = models.TextField()
#     country = models.CharField(max_length=200)
#     genre = models.CharField(max_length=100)
#     director = models.ForeignKey(Direcror,on_delete=models.PROTECT)
#     droduction = models.ForeignKey(Production,on_delete=models.PROTECT)
#     cast = models.ForeignKey(Cast,on_delete=models.PROTECT)
#     tag = models.ForeignKey(Tags,on_delete=models.PROTECT)
    

# for resturant

# class MenueIteams(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=True,decimal_places=True)
#     picture = models.ImageField(upload_to='person/',null=True,blank=True)
#     description = models.TextField()
#     cattegory = models.CharField(max_length=100)


# class Order(models.Model):
#     custumor = models.CharField(max_length=200)
#     iteams = models.ForeignKey(MenueIteams,on_delete=models.PROTECT)
#     total_price = models.DecimalField(max_digits=10,decimal_places=2)
#     satus = models.CharField(max_length=20,choices=[('pending','Pending'),('complated','completed')])
#     created_at = models.DateTimeField(auto_now_add=True)

























# class MovieCast(models.Model):
#     movie = models.ForeignKey(Movie,on_delete=models.PROTECT)
#     cast = models.ForeignKey(Cast,on_delete=models.PROTECT)

# class MovieTags(models.Model):
#     movie = models.ForeignKey(Movie,on_delete=models.PROTECT)
#     tag = models.ForeignKey(Tags, on_delete=models.PROTECT)
