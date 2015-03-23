from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form as Form


from mingtak.footer import MessageFactory as _


# Interface class; used to define content-type schema.

class IFooter(form.Schema, IImageScaleTraversable):
    """
    Footer setting
    """
    footerText = schema.Text(
        title=_(u"Footer Text"),
        required=False,
    )

    email = schema.TextLine(
       title=_(u"Contact email"),
        required=False,
    )

    facebookUrl = schema.URI(
        title=_(u"Facebook url"),
        required=False,
    )

    googlePlusUrl = schema.URI(
        title=_(u"GooglePlus url"),
        required=False,
    )

    twitterUrl = schema.URI(
        title=_(u"Twitter url"),
        required=False,
    )

    linkedIn = schema.URI(
        title=_(u"Linkedin url"),
        required=False,
    )


class Footer(Container):
    grok.implements(IFooter)



class FotterSettingControlPanelForm(RegistryEditForm):
    Form.extends(RegistryEditForm)
    schema = IFooter

FooterSettingControlPanelView = layout.wrap_form(FotterSettingControlPanelForm, ControlPanelFormWrapper)
FooterSettingControlPanelView.label = _(u"Footer setting")
