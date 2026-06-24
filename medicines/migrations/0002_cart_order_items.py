from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to=settings.AUTH_USER_MODEL)),

            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='medicines.cart')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicine')),
            ],
            options={
                'unique_together': {('cart', 'medicine')},
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='medicines.order')),
                ('medicine', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='medicines.medicine')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='medicine_name',
            field=models.CharField(max_length=200, default=''),
        ),
    ]

