from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
class Course_Instructor(AbstractBaseUser):
    user_id =models.SmallIntegerField(unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank= True, null=True)
    contact_no = models.BigIntegerField(unique=True,null=True, blank=True)
    desc= models.TextField(verbose_name=_('About Me'), null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='staff_pics')
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'


    def save(self,*args, **kwargs):
        super(Course_Instructor, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)