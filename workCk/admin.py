import builtins
from django.contrib import admin
from .models import Post
from .models import Work
from .models import Bussiness


admin.site.register(Post)
admin.site.register(Work)
admin.site.register(Bussiness)