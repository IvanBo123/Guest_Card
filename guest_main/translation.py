from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(About_usInfo)
class About_usInfoTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(StatisticInfo)
class StatisticInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'cent',)


@register(Type_ofCompanions)
class Type_ofCompanionsTranslationOptions(TranslationOptions):
    fields = ('types',)


@register(Companions)
class CompanionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)