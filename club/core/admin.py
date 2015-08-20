from django.contrib import admin

# Register your models here.
from core.models import (
	Player,
	Team,
	Fixtures,
	News,
	Gallery,
)


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Fixtures)
admin.site.register(News)
admin.site.register(Gallery)
