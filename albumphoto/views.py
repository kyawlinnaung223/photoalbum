from django.shortcuts import render,redirect
from .models import Category,Photo

# Create your views here.

#start gallery pageviews
def gallerypageivew(request):
          category=request.GET.get('category')
          if category == None:
                    photos=Photo.objects.all().order_by('-created')
          else:
                    photos=Photo.objects.filter(category__name__contains=category)
        
          
          categories=Category.objects.all()
          photo_count=photos.count()
          
          context={'categories':categories,'photos':photos,'photo_count':photo_count}
          return render(request,'photos/gallery.html',context)
#end gallery pageviews


#start photo pageviews
def photopageview(request, pk):
          photo=Photo.objects.get(id=pk)
          context={'photo':photo}
          return render(request,'photos/photo.html',context)
#end photo pageviews


#start add pageviews
def addpageview(request):
          
          categories=Category.objects.all()
          if request.method == 'POST':
                    data=request.POST
                    image=request.FILES.get('image')
                    
                    if data['category'] != 'none':
                              category=Category.objects.get(id=data['category'])
                    elif data['category-new'] != '':
                              category,created=Category.objects.get_or_create(
                                        name=data['category-new']
                              )
                    else:
                              category=none
                              
                    photo=Photo.objects.create(
                              category=category,
                              description=data['description'],
                              image=image,
                    )
                    
                    
                    return redirect('gallery')
                    
          context={'categories':categories}
          return render(request,'photos/add.html',context)
#end add pageviews
