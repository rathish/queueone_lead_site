from django.db import models
from django import forms

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcolumnblocks.blocks import ColumnsBlock

class CommonBlocks(blocks.StreamBlock):
    image = ImageChooserBlock(group="Common")
    content = blocks.RichTextBlock(group="Common")
    embed = EmbedBlock(group="Common")

class ColumnBlocks(blocks.StreamBlock):
    column_1_1 = ColumnsBlock(
        CommonBlocks(),
        ratios=(1, 1),
        label="Two halves",
        group="Columns",
    )
    
class HomePage(Page):
    pass
    
class QueueCallForAction(Page):
    text = models.CharField(max_length=255)
    
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
        
    url_link = models.URLField(blank=True, null=True)
    
    action_for = models.CharField(max_length=100, verbose_name='Action For',
        help_text="Action")
        
    content_panels = Page.content_panels + [
        FieldPanel('text'),
        ImageChooserPanel('image'),
        FieldPanel('url_link'),
        FieldPanel('action_for', widget=forms.Select(choices=(("Header", "Header"), \
            ("Timeline", "Timeline"), ("User", "User"), ("Partner", "Partner"),))),
       ] 
    
class QueueHeaderContainer(Page):
    content_1 = models.CharField(max_length=255)
    
    content_2 = models.CharField(max_length=255)

    content_3 = models.CharField(max_length=255)
    
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
    
    content_panels = Page.content_panels + [
        FieldPanel('content_1'),
        FieldPanel('content_2'),
        FieldPanel('content_3'),
        ImageChooserPanel('image'),
       ]  
    
class QueueWorkTimeline(Page):
    content = models.CharField(max_length=255)

    timeline_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
        
    order = models.PositiveIntegerField()

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        ImageChooserPanel('timeline_image'),
        FieldPanel('order'),
       ]
class QueueLinks(Page):
    text = models.CharField(max_length=50)
    
    url_link = models.URLField(blank=True, null=True)
    
    order = models.PositiveIntegerField(default = 0)
    
    content_panels = Page.content_panels + [
        FieldPanel('text'),
        FieldPanel('url_link'),
        FieldPanel('order'),
    ]  
    
class QueueOneSocialMedia(Page):
    icon = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
        
    url_link = models.URLField(blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('url_link'),
        ImageChooserPanel('icon'),
    ]  
    
class QueueOneLeadPage(Page):
    content_block = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('content', ColumnBlocks()),
    ], blank=True)
    
    logo_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
    
    content_panels = Page.content_panels + [
        ImageChooserPanel('logo_image'),
        StreamFieldPanel('content_block'),
        
      ]
      
    def get_user_benefits(self):
        return QueueUserBenefitsPage.objects.live().child_of(self).order_by('order')

    def get_partner_benefits(self):
        return QueuePartnerBenefitsPage.objects.live().child_of(self).order_by('order')

    def get_segments(self):
        return QueueSegments.objects.live().child_of(self)
        
    def get_work_statement(self):
        return QueueHeroStatement.objects.live().child_of(self).filter(statement_for = 'Works')
    def get_partner_statement(self):
        return QueueHeroStatement.objects.live().child_of(self).filter(statement_for = 'Partner')
    def get_user_statement(self):
        return QueueHeroStatement.objects.live().child_of(self).filter(statement_for = 'User')
        
    def get_all_work_line(self):
        return QueueWorkTimeline.objects.live().child_of(self).order_by('order')
        
    def get_header_container(self):
        return QueueHeaderContainer.objects.live().child_of(self)
        
    def get_call_action_header(self):
        return QueueCallForAction.objects.live().child_of(self).filter(action_for = 'Header')

    def get_call_action_timeline(self):
        return QueueCallForAction.objects.live().child_of(self).filter(action_for = 'Timeline')
        
    def get_social_media_links(self):
        return QueueOneSocialMedia.objects.live().child_of(self)
        
    def get_footer_links(self):
        return QueueLinks.objects.live().child_of(self).order_by('order')
        
class QueueHeroStatement(Page):
    statement = models.CharField(max_length=255)
    
    statement_for = models.CharField(max_length=100, verbose_name='Statement For',
        help_text="Statement for which section")
    
    content_panels = Page.content_panels + [
        FieldPanel('statement'),
        FieldPanel('statement_for', widget=forms.Select(choices=(("User", "User"), \
            ("Partner", "Partner"), ("Works", "Works"),))),
       ]

class QueueSegments(Page):
    segment = models.CharField(max_length=255)
    
    segment_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name='+')
    
    back_content = models.CharField(max_length=255)
    
    content_panels = Page.content_panels + [
        FieldPanel('segment'),
        ImageChooserPanel('segment_image'),
        FieldPanel('back_content')
       ]
       
class QueueUserBenefitsPage(Page):
    content_block = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('content', ColumnBlocks()),
    ], blank=True)

    order = models.PositiveIntegerField()

    content_panels = Page.content_panels + [
        StreamFieldPanel('content_block'),
        FieldPanel('order'),
      ] 


      
class QueuePartnerBenefitsPage(Page):
    content_block = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('content', ColumnBlocks()),
    ], blank=True)
    order = models.PositiveIntegerField()    
    content_panels = Page.content_panels + [
        StreamFieldPanel('content_block'),
        FieldPanel('order'),
      ] 

    
