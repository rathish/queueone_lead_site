# Generated by Django 2.0.6 on 2018-12-16 19:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0016_auto_20181216_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueueOneSocialMedia',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('url_link', models.URLField(blank=True, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
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