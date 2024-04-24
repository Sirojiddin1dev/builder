from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', )


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', )