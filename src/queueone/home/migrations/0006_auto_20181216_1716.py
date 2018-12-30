# Generated by Django 2.0.6 on 2018-12-16 17:16

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181216_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='queueherostatement',
            name='statement_for',
            field=models.CharField(default=1, help_text='Statement for which section', max_length=100, verbose_name='Statement For'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='queueoneleadpage',
            name='content_block',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('column_1_1', wagtail.core.blocks.StructBlock((('column_0', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common'))))), ('column_1', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common')))))), group='Columns', label='Two halves')),)))), blank=True),
        ),
        migrations.AlterField(
            model_name='queuepartnerbenefitspage',
            name='content_block',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('column_1_1', wagtail.core.blocks.StructBlock((('column_0', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common'))))), ('column_1', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common')))))), group='Columns', label='Two halves')),)))), blank=True),
        ),
        migrations.AlterField(
            model_name='queueuserbenefitspage',
            name='content_block',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.StreamBlock((('column_1_1', wagtail.core.blocks.StructBlock((('column_0', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common'))))), ('column_1', wagtail.core.blocks.StreamBlock((('image', wagtail.images.blocks.ImageChooserBlock(group='Common')), ('content', wagtail.core.blocks.RichTextBlock(group='Common')), ('embed', wagtail.embeds.blocks.EmbedBlock(group='Common')))))), group='Columns', label='Two halves')),)))), blank=True),
        ),
    ]
