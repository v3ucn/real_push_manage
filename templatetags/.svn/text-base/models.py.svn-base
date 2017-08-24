# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'categories'

class Collocation(models.Model):
    collocation_id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=420, blank=True)
    favorite = models.IntegerField(null=True, blank=True)
    tags = models.CharField(max_length=450, blank=True)
    image_id = models.IntegerField()
    isset = models.IntegerField()
    batch_no = models.IntegerField()
    draft = models.CharField(max_length=150, blank=True)
    isdraft = models.IntegerField(null=True, blank=True)
    style = models.IntegerField(null=True, blank=True)
    brands = models.CharField(max_length=6144, blank=True)
    categories = models.CharField(max_length=3072, blank=True)
    canvas_type = models.IntegerField(null=True, blank=True)
    activity_popular = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    isdelete = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=420, blank=True)
    class Meta:
        db_table = u'collocation'

class CommentCollocation(models.Model):
    comment_collocation_id = models.IntegerField(primary_key=True)
    collocation_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.CharField(max_length=3144)
    comment_date = models.DateTimeField()
    class Meta:
        db_table = u'comment_collocation'

class CommentItem(models.Model):
    comment_item_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.CharField(max_length=3144)
    comment_date = models.DateTimeField()
    class Meta:
        db_table = u'comment_item'

class Friends(models.Model):
    friends_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    friend_id = models.IntegerField(unique=True)
    familiar = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'friends'

class Images(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072)
    position = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'images'

class ItemCollocation(models.Model):
    item_collocation_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    collocation_id = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    left_margin = models.DecimalField(max_digits=22, decimal_places=15)
    top_margin = models.DecimalField(max_digits=22, decimal_places=15)
    width = models.IntegerField()
    height = models.IntegerField()
    zindex = models.IntegerField()
    batch_no = models.IntegerField()
    crop = models.CharField(max_length=150)
    class Meta:
        db_table = u'item_collocation'

class ItemImage(models.Model):
    item_image_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    image_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'item_image'

class ItemSet(models.Model):
    item_set_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    collocation_id = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    set_no = models.IntegerField(unique=True)
    left_margin = models.DecimalField(max_digits=22, decimal_places=15)
    top_margin = models.DecimalField(max_digits=22, decimal_places=15)
    width = models.IntegerField()
    height = models.IntegerField()
    batch_no = models.IntegerField(unique=True)
    crop = models.CharField(max_length=150)
    class Meta:
        db_table = u'item_set'

class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=768)
    source = models.CharField(max_length=192, blank=True)
    category = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=768, blank=True)
    orig_price = models.CharField(max_length=96, blank=True)
    curr_price = models.CharField(max_length=96, blank=True)
    brand = models.CharField(max_length=192, blank=True)
    pattern = models.CharField(max_length=96, blank=True)
    style = models.CharField(max_length=96, blank=True)
    design = models.CharField(max_length=48, blank=True)
    material = models.CharField(max_length=48, blank=True)
    properties = models.CharField(max_length=3072, blank=True)
    created = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=384, blank=True)
    description = models.CharField(max_length=6144, blank=True)
    activity_popular = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'items'

class Material(models.Model):
    material_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    url = models.CharField(max_length=3072)
    isbackground = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'material'

class MaterialCollocation(models.Model):
    material_collocation_id = models.IntegerField(primary_key=True)
    material_id = models.IntegerField()
    collocation_id = models.IntegerField()
    isbackground = models.IntegerField(null=True, blank=True)
    left_margin = models.DecimalField(max_digits=22, decimal_places=15)
    top_margin = models.DecimalField(max_digits=22, decimal_places=15)
    width = models.IntegerField()
    height = models.IntegerField()
    zindex = models.IntegerField()
    batch_no = models.IntegerField()
    class Meta:
        db_table = u'material_collocation'

class Materials(models.Model):
    materials_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072)
    class Meta:
        db_table = u'materials'

class Notice(models.Model):
    notice_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=6144)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'notice'

class Sale(models.Model):
    item_id = models.IntegerField(null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)
    orig_price = models.IntegerField(null=True, blank=True)
    curr_price = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=96, blank=True)
    sale_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'sale'

class Search(models.Model):
    search_id = models.IntegerField(primary_key=True)
    search_type = models.IntegerField(null=True, blank=True)
    search_name = models.CharField(max_length=60, blank=True)
    chinese_name = models.CharField(max_length=60, blank=True)
    other_name = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'search'

class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=15, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tag'

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=60)
    password = models.CharField(max_length=300)
    sex = models.IntegerField(null=True, blank=True)
    email = models.CharField(unique=True, max_length=150)
    fan_words = models.CharField(max_length=600, blank=True)
    location = models.CharField(max_length=150, blank=True)
    education = models.CharField(max_length=60, blank=True)
    career = models.CharField(max_length=60, blank=True)
    salary = models.CharField(max_length=60, blank=True)
    likes = models.CharField(max_length=1200, blank=True)
    avatar = models.IntegerField(null=True, blank=True)
    register_date = models.DateTimeField()
    last_login = models.DateTimeField()
    visit = models.IntegerField()
    income = models.IntegerField()
    isdeleted = models.IntegerField(null=True, blank=True)
    nosay = models.IntegerField(null=True, blank=True)
    isactive = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user'

class UserCollocation(models.Model):
    user_collocation_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    collocation_id = models.IntegerField(unique=True)
    isown = models.IntegerField(null=True, blank=True)
    isfavorite = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_collocation'

class UserItem(models.Model):
    user_item_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    item_id = models.IntegerField(unique=True)
    collect_date = models.DateTimeField()
    class Meta:
        db_table = u'user_item'

class UserMaterial(models.Model):
    user_material_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    material_id = models.IntegerField()
    isown = models.IntegerField()
    isfavorite = models.IntegerField()
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_material'

