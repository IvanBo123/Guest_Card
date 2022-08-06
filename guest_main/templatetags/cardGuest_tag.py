from django import template
from guest_main.models import About_usInfo

register = template.Library()


@register.simple_tag()
def get_About_usInfo():
    """Вывод всех категорий"""
    return About_usInfo.objects.all()


@register.simple_tag()
def get_StatisticInfo():
    """Вывод всех категорий"""
    return StatisticInfo.objects.all()


@register.simple_tag()
def get_Type_ofCompanions():
    """Вывод всех категорий"""
    return Type_ofCompanions.objects.all()


@register.simple_tag()
def get_Companions():
    """Вывод всех категорий"""
    return Companions.objects.all()


@register.inclusion_tag('guest_main/main.html')
def get_template(count=5):
    about_us = About_usInfo.objects.order_by("id")[:count]
    statistic = StatisticInfo.objects.order_by("id")[:count]
    types = Type_ofCompanions.objects.order_by("id")[:count]
    companions = Companions.objects.order_by("id")[:count]
    return {"about_us": about_us,
            "statistic": statistic,
            "types": types,
            "companions": companions,
    }
