import calendar

from django import template


register = template.Library()


@register.assignment_tag
def get_goal_difference(goal_for, goal_against):
    goal_diff = goal_for - goal_against
    return goal_diff


@register.assignment_tag
def get_month(fixture):
	if fixture:
		fix = fixture[0]
		year = fix.date.year
		month_number = fix.date.month
		month = calendar.month_name[month_number]
		month_year = [month, year]
		return month_year
	return None
