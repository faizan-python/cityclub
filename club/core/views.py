from django.shortcuts import render

from core.models import (
    Team,
    Player,
    Fixtures,
    News,
    Gallery,
)


def get_player_by_group():
    defenders = Player.objects.filter(position="Defender")
    goalkeepers = Player.objects.filter(position="Goalkeeper")
    strikers = Player.objects.filter(position="Strikers")
    midfielders = Player.objects.filter(position="Midfielder")
    
    players = [goalkeepers, defenders, midfielders, strikers]
    return players


def index(request):
    team_point_table = Team.objects.all().order_by("name")[:10]
    
    players = Player.objects.filter()[:7]
    news = News.objects.filter()[:4]
    results = []
    i=1
    for team in team_point_table:
        results.append({
            'name': team.name,
            'points': team.points,
            'game_won': team.game_won,
            'game_lost': team.game_lost,
            'position': i
        })
        i += 1

    fixture = Fixtures.objects.all().order_by("date")[:8]
    images = Gallery.objects.all()
    players_by_group = get_player_by_group()
    latest_fixtures = Fixtures.objects.all().order_by("date")[:1]

    return render(request, 'core/demo.html', {'team_point_table' : results,
    	                                      'players': players,
    	                                      'fixtures': fixture,
    	                                      'players_by_group': players_by_group,
                                              'news': news,
                                              'images': images,
                                              'latest_fixtures': latest_fixtures})


def league_table(request):
    team_point_table = Team.objects.all().order_by("name")
    print "helloooo",len(team_point_table)
    results = []
    i=1
    for team in team_point_table:
        results.append({
            'name': team.name,
            'points': team.points,
            'game_won': team.game_won,
            'game_lost': team.game_lost,
            'position': i,
            'game_played': team.game_played,
            'goal_conceded': team.goal_conceded,
            'goal_scored': team.goal_scored,
            'game_draw': team.game_draw
        })
        i += 1
    
    players_by_group = get_player_by_group()
    return render(request, 'core/league_table.html', {'team_point_table' : results,
    	                                              'players_by_group': players_by_group})


def team(request):
    goalkeepers = Player.objects.filter(position="Goalkeeper")
    players = [goalkeepers]
    players_by_group = get_player_by_group()

    return render(request, 'core/team.html', {'players': players, "active_tab": "GK",
    	                                      'players_by_group': players_by_group})


def defender(request):
    defenders = Player.objects.filter(position="Defender")
    players = [defenders]
    players_by_group = get_player_by_group()

    return render(request, 'core/team.html', {'players': players, "active_tab": "DF",
    	                                      'players_by_group': players_by_group})


def midfielder(request):
    midfielders = Player.objects.filter(position="Midfielder")
    players = [midfielders]
    players_by_group = get_player_by_group()

    return render(request, 'core/team.html', {'players': players, "active_tab": "MD",
    	                                      'players_by_group': players_by_group})


def striker(request):
    strikers = Player.objects.filter(position="Striker")
    players = [strikers]
    players_by_group = get_player_by_group()

    return render(request, 'core/team.html', {'players': players, "active_tab": "ST",
    	                                      'players_by_group': players_by_group})


def contact_us(request):
    players_by_group = get_player_by_group()

    return render(request, 'core/contactus.html', {'players_by_group': players_by_group})


def fixture_result(request):
    july_result = Fixtures.objects.filter(date__year=2015, date__month=7)
    aug_result = Fixtures.objects.filter(date__year=2015, date__month=8)
    sep_result = Fixtures.objects.filter(date__year=2015, date__month=9)
    oct_result = Fixtures.objects.filter(date__year=2015, date__month=10)
    nov_result = Fixtures.objects.filter(date__year=2015, date__month=11)
    dec_result = Fixtures.objects.filter(date__year=2015, date__month=12)
    jan_result = Fixtures.objects.filter(date__year=2016, date__month=1)
    feb_result = Fixtures.objects.filter(date__year=2016, date__month=2)
    mar_result = Fixtures.objects.filter(date__year=2016, date__month=3)
    apr_result = Fixtures.objects.filter(date__year=2016, date__month=4)
    may_result = Fixtures.objects.filter(date__year=2016, date__month=5)
    june_result = Fixtures.objects.filter(date__year=2016, date__month=6)
    
    result = [july_result, aug_result,sep_result,oct_result,nov_result,dec_result,jan_result,feb_result,
              mar_result,apr_result,may_result,june_result]

    players_by_group = get_player_by_group() 
    return render(request, 'core/fixtures.html', {'result': result,
    	                                          'players_by_group': players_by_group})


def user_detail(request, user_id):
    player = Player.objects.get(id=user_id)

    players_by_group = get_player_by_group()
    return render(request, 'core/player_detail.html', {'player': player,
    	                                               'players_by_group': players_by_group})


def news(request, news_id):
    news = News.objects.get(id=news_id)
    players_by_group = get_player_by_group()
    return render(request, 'core/news.html', {'news': news,
                                              'players_by_group': players_by_group})


def news_all(request):
    news = News.objects.all()
    players_by_group = get_player_by_group()
    return render(request, 'core/news-all.html', {'news': news,
                                                  'players_by_group': players_by_group})


def gallery(request):
    images = Gallery.objects.all()
    players_by_group = get_player_by_group()
    return render(request, 'core/gallery.html', {'images': images,
                                                 'players_by_group': players_by_group})
