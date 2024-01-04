from datetime import timezone
from django.db import models

# for the following model we first create Post model which will allows user to post things into the the blog
# The Post will have a title, slug and body. More information on each later
class Post(models.Model):
    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 250)
    body = models.TextField()

    # ADDED publishing, create and update
    publish = models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    # ADDED default sorting

    class Meta:
        ordering = ['-publish']



    def __str__(self):
        return self.title
    

    

    # 
    # title: this is the field for posts title. The field is CharField which translates to VARCHAR in normal SQL syntax
    # slug: this is a SlugField which translates to VARCHAR in normal SQL syntax. A slug field is short label for short labels that contain leters, numbers and underscores or hyphens.
    # body: this is a field for storing body of the post. It is a TextField which translates to Text column in normal SQL syntax.


    # also we have added a __str__() method this is a default method to return a string with the human readable representation of the object.
    #  Django will use this method to display the name of the object name of the object in many places such as the admin site.

    ###################################################################

    #ADDING datetime FIELDS 
    # publish: this is a DateTimeField that translates to DATETIME in sql syntax. It will be used to store time the dates blogs were published.
        # timezone now returns the current time.
    # created: also witha DateTimeField that translates to DATETIME in sql syntax. By using auto_now_add the dates are saved automatically. stores date blog was created.
    # updated: also with a DateTimeField that translates to DATETIME in sql syntax. By using auto_now_add the dates are saved automatically.stores last date and tiem the blog was updated.
    
    

    # The Meta class defines the meta data for the model. We also use the ordering attribute to tell django to sort results by the publish field. 
        # the order will apply be default for database queries when no specific order is specified. we also indicate it will in descending order by using the hyphen. 
        # They will be returned in reverse order
        