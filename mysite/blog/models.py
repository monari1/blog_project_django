# from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# the custom model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)

# for the following model we first create Post model which will allows user to post things into the the blog
# The Post will have a title, slug and body. More information on each later (part 1)

class Post(models.Model):
    # ............ PART 5 ...............
    class Status (models.TextChoices):
        DRAFT = 'DF', "DRAFT"
        PUBLISHED = "PB", "PUBLISHED"

    # ............ END PART 5 ..........
        
    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 250)
    body = models.TextField()

    # ADDED publishing, create and update (part 2)
    publish = models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    # ADDED default sorting and index
    # part 7
    author = models.ForeignKey(User, 
                               on_delete= models.CASCADE, 
                               related_name="blog_posts")
    # part 6
    status = models.CharField(max_length=2,
                              choices = Status.choices,
                              default = Status.DRAFT)
    objects = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager

    class Meta:
        # part 3
        ordering = ['-publish']
        # Added the index (check notes part 4)
        indexes = [
            models.Index(fields=['-publish'])]



    def __str__(self):
        return self.title
    



    

    

    # ............. Part 1 (Creating the  Post model)....................
    # title: this is the field for posts title. The field is CharField which translates to VARCHAR in normal SQL syntax
    # slug: this is a SlugField which translates to VARCHAR in normal SQL syntax. A slug field is short label for short labels that contain leters, numbers and underscores or hyphens.
    # body: this is a field for storing body of the post. It is a TextField which translates to Text column in normal SQL syntax.


    # also we have added a __str__() method this is a default method to return a string with the human readable representation of the object.
    #  Django will use this method to display the name of the object name of the object in many places such as the admin site.

    # ................ Part 2 (Adding datetime fields)......................

    #ADDING datetime FIELDS 
    # publish: this is a DateTimeField that translates to DATETIME in sql syntax. It will be used to store time the dates blogs were published.
        # timezone now returns the current time.
    # created: also witha DateTimeField that translates to DATETIME in sql syntax. By using auto_now_add the dates are saved automatically. stores date blog was created.
    # updated: also with a DateTimeField that translates to DATETIME in sql syntax. By using auto_now_add the dates are saved automatically.stores last date and tiem the blog was updated.
    
    # .............. Part 3 (Defining the default sort) .................... 

    # The Meta class defines the meta data for the model. We also use the ordering attribute to tell django to sort results by the publish field. 
        # the order will apply be default for database queries when no specific order is specified. we also indicate it will in descending order by using the hyphen. 
        # They will be returned in reverse order
    
    # ................ Part 4 (Adding a database indexes) ........................
    # The index option has been added to the model's meta class. The option allows you to define the database index fo the model, this could compromise multiple fields in the.
    # in ascending order or descending or functional expression and database functions. 
    # The creation of index will be included in the migrations

    # .................... Part 5 (Enum) ......................
    # The enumeration subclass is defined as Status by (models.TextChoices).  The choices available are DRAFT and PUBLISHED. Check on enum class from documentation.

    # ................... Part 6 (Status field) ................
    # we have also added the status field which is an instance of CharField. It has the choices parameter to limit value of choices to only the choices in Status.choices. 
    # we have also set the default for the field to using default parameter and DRAFT is the default. 

    # .................... Part 7 (Many-to-One Relationship) --------------------------------
    # So the the django authentication comes with User which contains the many-to-one relationship
    # so we have defined the author which means the user can have many posts thus the many-to-one relationship. 

        