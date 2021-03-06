from Products.validation.interfaces.IValidator import IValidator
from Products.validation import validation
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFPlone.utils import safe_unicode
from PIL import Image
from types import ListType, TupleType
from five import grok
from plone.registry.interfaces import IRegistry
from wcc.carousel import MessageFactory as _
from zope.interface import implements, Invalid

def validate_image(image_file):
#    width = 510
#    height = 330
#    return _validate_image(image_file, width, height)
    return True

def _validate_image(image_file, width, height):
    try:
        image_file.seek(0)
        image = Image.open(image_file)
        w = image.size[0]
        h = image.size[1]
        if w != width or h != height:
            return _(u'Invalid size. Please upload %sx%s image' % (width,
                height))
    except:
        # had issue with validation of size, ignore.. probably should do
        # something here
        pass

    return True

class ArchetypeImageSizeValidator(object):
    implements(IValidator)

    name = 'wcc.carousel.validator.ImageConstraintValidator'

    def __call__(self, value, *args, **kwargs):
        result = validate_image(value)
        return result

validation.register(ArchetypeImageSizeValidator())

class DexterityImageSizeValidator(object):

    def validate(self, value):
        result = validate_image(value.open())
        if result is not True:
            raise Invalid(result)
        return True

