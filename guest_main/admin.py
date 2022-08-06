from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import *


# Register your models here.
class About_usInfoAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget())
    description_uz = forms.CharField(label="Tasvir", widget=CKEditorUploadingWidget())

    class Meta:
        model = About_usInfo
        fields = '__all__'


class StatisticInfoAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget())
    description_uz = forms.CharField(label="Tasvir", widget=CKEditorUploadingWidget())

    class Meta:
        model = StatisticInfo
        fields = '__all__'


class Type_ofCompanionsAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget())
    description_uz = forms.CharField(label="Tasvir", widget=CKEditorUploadingWidget())

    class Meta:
        model = Type_ofCompanions
        fields = '__all__'


class CompanionsAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget())
    description_uz = forms.CharField(label="Tasvir", widget=CKEditorUploadingWidget())

    class Meta:
        model = Companions
        fields = '__all__'


class about_usInfoAdmin(TranslationAdmin):
    list_display = ('description', 'image',)


admin.site.register(About_usInfo, about_usInfoAdmin)


class StatisticInfoAdmin(TranslationAdmin):
    list_display = ('name', 'href', 'value', 'cent',)


admin.site.register(StatisticInfo, StatisticInfoAdmin)


class Type_ofCompanionsAdmin(TranslationAdmin):
    list_display = ('types', 'tag')


admin.site.register(Type_ofCompanions, Type_ofCompanionsAdmin)


class CompanionsAdmin(TranslationAdmin):
    list_display = ('name', 'status', 'description',
                    'image', 'type_of', 'href')
    list_filter = ('type_of',)


admin.site.register(Companions, CompanionsAdmin)


class Social_HubsAdmin(admin.ModelAdmin):
    list_display = ('icon', 'href')


admin.site.register(Social_Hubs, Social_HubsAdmin)
