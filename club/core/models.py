from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=128)
    weight = models.IntegerField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=128, default="Indian")
    jersey_number = models.IntegerField(null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    picture = models.ImageField(upload_to="pictures", null=True, blank=True, default = 'pictures/default3.png')

    class Meta:
        verbose_name_plural = 'Players'

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128)
    points = models.IntegerField(blank=True)
    game_lost = models.IntegerField(blank=True)
    game_played = models.IntegerField(blank=True)
    game_won = models.IntegerField(blank=True)
    game_draw = models.IntegerField(blank=True)
    goal_scored = models.IntegerField(blank=True)
    goal_conceded = models.IntegerField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Teams'

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=128, default="Admin@CityClub")
    date = models.DateTimeField(blank=True)
    picture = models.ImageField(upload_to="news_pictures", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title


class Fixtures(models.Model):
    home_team = models.ForeignKey(Team, related_name="Home_Team")
    away_team = models.ForeignKey(Team, related_name="Away_Team")
    score = models.CharField(max_length=128, blank=True)
    goal_scored_home = models.IntegerField(blank=True)
    goal_scored_away = models.IntegerField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    game_played = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Fixtures'

    def __unicode__(self):
        return self.score


class Gallery(models.Model):
    picture = models.ImageField(upload_to="gallery", null=True, blank=True)
    picture_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __unicode__(self):
        return self.picture_name
