# Generated by Django 3.2.8 on 2021-10-09 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('Sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=50, null=True)),
                ('Address', models.CharField(default='El-wiam', max_length=200, null=True)),
                ('city', models.CharField(default='Sidi bel-abbes', max_length=200, null=True)),
                ('county', models.CharField(default='Algérie', max_length=200, null=True)),
                ('code', models.CharField(default='1500', max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed'), ('Delayed', 'Delayed'), ('Pending', 'Pending')], max_length=15)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(default='black', max_length=200, null=True)),
                ('price', models.FloatField(default=200)),
                ('old_price', models.FloatField(blank=True, default=100)),
                ('Product_details', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_archived', models.BooleanField(blank=True, default=True, null=True)),
                ('is_top_selling', models.BooleanField(blank=True, default=True, null=True)),
                ('is_top_ranking', models.BooleanField(blank=True, default=True, null=True)),
                ('is_flash_deal', models.BooleanField(blank=True, default=True, null=True)),
                ('is_garanted', models.BooleanField(blank=True, default=True, null=True)),
                ('is_new', models.BooleanField(blank=True, default=True, null=True)),
                ('is_promo', models.BooleanField(blank=True, default=False, null=True)),
                ('remise', models.IntegerField(default=10, null=True)),
                ('Camera', models.CharField(blank=True, choices=[('up to 2.9 MP', 'up to 2.9 MP'), ('3 to 4.9 MP', '3 to 4.9 MP'), ('5 to 7.9 MP', '5 to 7.9 MP'), ('8 to 12.9 MP', '8 to 12.9 MP'), ('13 to 19.9 MP', '13 to 19.9 MP'), ('20 MP and above', '20 MP and above')], max_length=100, null=True)),
                ('Cam', models.IntegerField(blank=True, default=15, null=True)),
                ('Memory', models.CharField(blank=True, choices=[('4Go', '4Go'), ('8Go', '8Go'), ('16Go', '16Go'), ('32Go', '32Go'), ('64Go', '64Go'), ('128Go', '128Go'), ('256Go', '256Go'), ('1To', '1To')], max_length=100, null=True)),
                ('System', models.CharField(blank=True, choices=[('Android', 'Android'), ('IOS', 'IOS'), ('Fire', 'Fire'), ('Linux', 'Linux'), ('Windows', 'Windows')], max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('Processor', models.CharField(blank=True, max_length=100, null=True)),
                ('battery', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='mystella.brand')),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to='mystella.catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.customer')),
            ],
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.product')),
                ('wish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.wish')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('Sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=200)),
                ('Address', models.CharField(max_length=200, null=True)),
                ('is_admin', models.BooleanField(blank=True, default=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='ryad', max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.CharField(default='niceproduct', max_length=1000, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=3)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mystella.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystella.product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mystella.product')),
            ],
        ),
    ]
