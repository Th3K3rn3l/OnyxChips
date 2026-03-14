from django.contrib import admin

# Register your models here.
from main.models import User, Game, GameSession, Transaction

admin.site.register(User)
admin.site.register(Game)
admin.site.register(GameSession)
admin.site.register(Transaction)