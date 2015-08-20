# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.CharField(max_length=128, blank=True)),
                ('goal_scored_home', models.IntegerField(blank=True)),
                ('goal_scored_away', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('game_played', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Fixtures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(default=b'Admin@CityClub', max_length=128)),
                ('date', models.DateTimeField(blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'news_pictures', blank=True)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('position', models.CharField(max_length=128)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('nationality', models.CharField(default=b'Indian', max_length=128)),
                ('jersey_number', models.IntegerField(null=True, blank=True)),
                ('picture', models.ImageField(default=b'pictures/default3.png', null=True, upload_to=b'pictures', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('points', models.IntegerField(blank=True)),
                ('game_lost', models.IntegerField(blank=True)),
                ('game_played', models.IntegerField(blank=True)),
                ('game_won', models.IntegerField(blank=True)),
                ('game_draw', models.IntegerField(blank=True)),
                ('goal_scored', models.IntegerField(blank=True)),
                ('goal_conceded', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fixtures',
            name='away_team',
            field=models.ForeignKey(related_name=b'Away_Team', to='core.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fixtures',
            name='home_team',
            field=models.ForeignKey(related_name=b'Home_Team', to='core.Team'),
            preserve_default=True,
        ),
    ]
