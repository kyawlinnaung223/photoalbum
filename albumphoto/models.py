from django.db import models

# Create your models here.


# this is category models
class Category(models.Model):
          name=models.CharField(max_length=200, blank=True,null=True)
          def __str__(self):
                    return self.name
# end


#this is photo models

class Photo(models.Model):
          category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
          image=models.ImageField(null=False,blank=False)
          description=models.TextField()
          update= models.DateTimeField(auto_now=True ,blank=True ,null=True)
          created=models.DateTimeField(auto_now_add=True,blank=True ,null=True)
          
          def __str__(self):
                    return self.description
#end
