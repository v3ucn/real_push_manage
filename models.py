# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Action(models.Model):
    action_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    target_id = models.IntegerField()
    feed_type = models.IntegerField()
    action_type = models.IntegerField(null=True, blank=True)
    action = models.CharField(max_length=450, blank=True)
    class Meta:
        db_table = u'action'

class AdminJob(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField(null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)
    itemid = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'admin_job'

class AdminUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=768, blank=True)
    nickname = models.CharField(max_length=768, blank=True)
    role = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'admin_user'

class Avatar(models.Model):
    avatar_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072)
    position = models.IntegerField()
    class Meta:
        db_table = u'avatar'

class Blog(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150, blank=True)
    content = models.CharField(max_length=12288, blank=True)
    theme = models.CharField(max_length=450, blank=True)
    batch_no = models.IntegerField()
    pictures = models.IntegerField(null=True, blank=True)
    forward = models.IntegerField(null=True, blank=True)
    favorite = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    status = models.IntegerField(null=True, blank=True)
    isdraft = models.IntegerField()
    isdelete = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'blog'

class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'categories'

class Collocation(models.Model):
    collocation_id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=6144, blank=True)
    favorite = models.IntegerField(null=True, blank=True)
    theme = models.CharField(max_length=300, blank=True)
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
    istalent = models.IntegerField(null=True, blank=True)
    isself = models.IntegerField(null=True, blank=True)
    isstreet = models.IntegerField(null=True, blank=True)
    isstar = models.IntegerField(null=True, blank=True)
    look_id = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    template_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'collocation'

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    target_id = models.IntegerField()
    comment_type = models.IntegerField()
    comment = models.CharField(max_length=3144)
    comment_date = models.DateTimeField()
    class Meta:
        db_table = u'comment'

class CommentBlog(models.Model):
    comment_blog_id = models.IntegerField(primary_key=True)
    blog_id = models.IntegerField()
    user_id = models.IntegerField()
    comment = models.CharField(max_length=3072)
    comment_date = models.DateTimeField()
    class Meta:
        db_table = u'comment_blog'

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

class Cut(models.Model):
    cut_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    iscut = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'cut'

class Editor(models.Model):
    editor_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=768, blank=True)
    realname = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'editor'

class Fan(models.Model):
    fan_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    cover_id = models.IntegerField()
    position = models.IntegerField()
    fan_type = models.IntegerField()
    themed = models.IntegerField(null=True, blank=True)
    ishome = models.IntegerField(null=True, blank=True)
    comment_count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'fan'

class FanTheme(models.Model):
    fan_theme_id = models.IntegerField(primary_key=True)
    fan_id = models.IntegerField()
    cover_id = models.IntegerField()
    name = models.CharField(max_length=30, blank=True)
    position = models.IntegerField()
    ishome = models.IntegerField(null=True, blank=True)
    comment_count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'fan_theme'

class Fashion(models.Model):
    fashion_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=450, blank=True)
    description = models.CharField(max_length=3072, blank=True)
    tags = models.CharField(max_length=450, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    pictures = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=60, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    sort = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'fashion'

class Feed(models.Model):
    feed_id = models.IntegerField(primary_key=True)
    target_id = models.IntegerField()
    user_id = models.IntegerField()
    parent_id = models.IntegerField()
    feed_type = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=450, blank=True)
    theme = models.CharField(max_length=450, blank=True)
    publish_date = models.DateTimeField()
    ishome = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    username = models.CharField(max_length=60, blank=True)
    content = models.CharField(max_length=6144, blank=True)
    class Meta:
        db_table = u'feed'

class Figure(models.Model):
    figure_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=420, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    fashion_id = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    collocation_id = models.IntegerField(null=True, blank=True)
    template_id = models.IntegerField(null=True, blank=True)
    iscollocation = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'figure'

class Friends(models.Model):
    friends_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    friend_id = models.IntegerField(unique=True)
    familiar = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'friends'

class Gosee(models.Model):
    gosee_id = models.IntegerField(primary_key=True)
    pictorial_id = models.IntegerField()
    item_id = models.IntegerField()
    image_id = models.IntegerField()
    left_margin = models.IntegerField(null=True, blank=True)
    top_margin = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'gosee'

class Images(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072)
    position = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'images'

class ItemCollocation(models.Model):
    item_collocation_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    collocation_id = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    left_margin = models.IntegerField()
    top_margin = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    zindex = models.IntegerField()
    crop = models.CharField(max_length=150)
    rotation = models.IntegerField()
    flop = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'item_collocation'

class ItemCollocationOrig(models.Model):
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
        db_table = u'item_collocation_orig'

class ItemImage(models.Model):
    item_image_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    image_id = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'item_image'

class ItemPictorial(models.Model):
    item_pictorial_id = models.IntegerField(primary_key=True)
    pictorial_id = models.IntegerField()
    left_margin = models.IntegerField(null=True, blank=True)
    top_margin = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    gosee_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'item_pictorial'

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

class ItemTemplate(models.Model):
    item_template_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    template_id = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    left_margin = models.IntegerField()
    top_margin = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    zindex = models.IntegerField()
    crop = models.CharField(max_length=150)
    rotation = models.IntegerField()
    flop = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'item_template'

class Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    url = models.CharField(unique=True, max_length=765, blank=True)
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
    review = models.IntegerField(null=True, blank=True)
    expire = models.IntegerField(null=True, blank=True)
    xiupian = models.IntegerField(null=True, blank=True)
    beijing = models.IntegerField(null=True, blank=True)
    homed = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    reason = models.CharField(max_length=144, blank=True)
    recommend = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'items'

class JobFt(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    shu = models.IntegerField(null=True, blank=True)
    date = models.CharField(max_length=768, blank=True)
    realname = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'job_ft'

class LiveImg(models.Model):
    id = models.IntegerField(primary_key=True)
    image_id = models.IntegerField()
    item_id = models.IntegerField()
    class Meta:
        db_table = u'live_img'

class Looks(models.Model):
    look_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072)
    position = models.IntegerField()
    class Meta:
        db_table = u'looks'

class Magazine(models.Model):
    magazine_id = models.IntegerField(primary_key=True)
    phase = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=3072, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    cover_id = models.IntegerField(null=True, blank=True)
    ishome = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'magazine'

class Material(models.Model):
    material_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    url = models.CharField(max_length=3072)
    isbackground = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    ishome = models.IntegerField(null=True, blank=True)
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
    item_id = models.IntegerField(null=True, blank=True)
    image_id = models.IntegerField(null=True, blank=True)
    rotation = models.IntegerField(null=True, blank=True)
    flop = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'material_collocation'

class MaterialTemplate(models.Model):
    material_template_id = models.IntegerField(primary_key=True)
    material_id = models.IntegerField()
    item_id = models.IntegerField(null=True, blank=True)
    image_id = models.IntegerField(null=True, blank=True)
    template_id = models.IntegerField()
    isbackground = models.IntegerField(null=True, blank=True)
    left_margin = models.IntegerField()
    top_margin = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    zindex = models.IntegerField()
    rotation = models.IntegerField()
    flop = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'material_template'

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

class Photo(models.Model):
    photo_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=420, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    talent_id = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    collocation_id = models.IntegerField(null=True, blank=True)
    template_id = models.IntegerField(null=True, blank=True)
    iscollocation = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'photo'

class Pictorial(models.Model):
    pictorial_id = models.IntegerField(primary_key=True)
    magazine_id = models.IntegerField()
    position = models.IntegerField()
    title = models.CharField(max_length=3072, blank=True)
    url = models.CharField(max_length=3072, blank=True)
    ishome = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=6144, blank=True)
    email = models.CharField(max_length=150, blank=True)
    theme = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'pictorial'

class Pictresult(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.IntegerField(null=True, blank=True)
    result = models.TextField(blank=True)
    class Meta:
        db_table = u'pictresult'

class Pictures(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=3072, blank=True)
    description = models.CharField(max_length=600, blank=True)
    position = models.IntegerField(null=True, blank=True)
    batch_no = models.IntegerField()
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pictures'

class Qa(models.Model):
    qa_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=450, blank=True)
    description = models.CharField(max_length=3072, blank=True)
    tags = models.CharField(max_length=150, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    pictures = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=60, blank=True)
    isqa = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    target_id = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'qa'

class Qaimages(models.Model):
    qaimages_id = models.IntegerField(primary_key=True, db_column='qaImages_id') # Field name made lowercase.
    title = models.CharField(max_length=420, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    qa_id = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    collocation_id = models.IntegerField(null=True, blank=True)
    template_id = models.IntegerField(null=True, blank=True)
    iscollocation = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'qaimages'

class Recommend(models.Model):
    recommend_id = models.IntegerField(primary_key=True)
    target_id = models.IntegerField(null=True, blank=True)
    feed_type = models.IntegerField()
    position = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'recommend'

class RecommendFeed(models.Model):
    recommend_feed_id = models.IntegerField(primary_key=True)
    target_id = models.IntegerField()
    user_id = models.IntegerField()
    parent_id = models.IntegerField()
    feed_type = models.IntegerField()
    image_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=450, blank=True)
    theme = models.CharField(max_length=450, blank=True)
    publish_date = models.DateTimeField()
    height = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    content = models.CharField(max_length=6144, blank=True)
    class Meta:
        db_table = u'recommend_feed'

class RecommendItem(models.Model):
    recommend_item_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    image_id = models.IntegerField()
    recommend_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'recommend_item'

class RecommendPictorial(models.Model):
    recommend_pictorial_id = models.IntegerField(primary_key=True)
    reason = models.CharField(max_length=300, blank=True)
    pictorial_id = models.IntegerField()
    user_id = models.IntegerField()
    recommend_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'recommend_pictorial'

class RecommendUser(models.Model):
    recommend_user_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    ishome = models.IntegerField(null=True, blank=True)
    word = models.CharField(max_length=300, blank=True)
    search = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=768, blank=True)
    recommend_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'recommend_user'

class Sale(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)
    orig_price = models.IntegerField(null=True, blank=True)
    curr_price = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'sale'

class Score(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    target_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'score'

class Search(models.Model):
    search_id = models.IntegerField(primary_key=True)
    search_type = models.IntegerField(null=True, blank=True)
    little_type = models.IntegerField(null=True, blank=True)
    search_name = models.CharField(max_length=600, blank=True)
    show_name = models.CharField(max_length=300, blank=True)
    other_name = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'search'

class Stable(models.Model):
    id = models.IntegerField(primary_key=True)
    rowid = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'stable'

class Storage(models.Model):
    storage_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=768, blank=True)
    user_id = models.IntegerField()
    reason = models.CharField(max_length=3072, blank=True)
    publish_date = models.DateTimeField()
    scraped = models.IntegerField(null=True, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    tags = models.CharField(max_length=144, blank=True)
    class Meta:
        db_table = u'storage'

class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=15, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tag'

class Talent(models.Model):
    talent_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=420, blank=True)
    description = models.CharField(max_length=3072, blank=True)
    tags = models.CharField(max_length=150, blank=True)
    height = models.IntegerField(null=True, blank=True)
    pictures = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=60)
    isdelete = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'talent'

class Template(models.Model):
    template_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=3072, blank=True)
    ishome = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=768, blank=True)
    html = models.CharField(max_length=768, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'template'

class Uploadlog(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField(null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)
    itemid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'uploadlog'

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
    login = models.CharField(max_length=300, blank=True)
    avata = models.IntegerField(null=True, blank=True)
    tags = models.CharField(max_length=3072, blank=True)
    url = models.CharField(max_length=768, blank=True)
    token = models.CharField(max_length=768, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user'

class UserAvatar(models.Model):
    user_avatar_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True, null=True, blank=True)
    avatar_id = models.IntegerField(unique=True, null=True, blank=True)
    class Meta:
        db_table = u'user_avatar'

class UserBlog(models.Model):
    user_blog_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    blog_id = models.IntegerField()
    isown = models.IntegerField()
    isfavorite = models.IntegerField()
    publish_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'user_blog'

class UserCollocation(models.Model):
    user_collocation_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    collocation_id = models.IntegerField(unique=True)
    isown = models.IntegerField(null=True, blank=True)
    isfavorite = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    isset = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_collocation'

class UserFashion(models.Model):
    user_fashion_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    fashion_id = models.IntegerField()
    state = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_fashion'

class UserFeed(models.Model):
    user_feed_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    target_id = models.IntegerField()
    state = models.IntegerField(null=True, blank=True)
    feed_type = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_feed'

class UserItem(models.Model):
    user_item_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    item_id = models.IntegerField(unique=True)
    collect_date = models.DateTimeField()
    state = models.IntegerField(null=True, blank=True)
    item_type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_item'

class UserMaterial(models.Model):
    user_material_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    material_id = models.IntegerField()
    isown = models.IntegerField()
    isfavorite = models.IntegerField()
    publish_date = models.DateTimeField()
    isbackground = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_material'

class UserQa(models.Model):
    user_qa_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    qa_id = models.IntegerField()
    state = models.IntegerField(null=True, blank=True)
    isqa = models.IntegerField(null=True, blank=True)
    isdelete = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_qa'

class UserTalent(models.Model):
    user_talent_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    talent_id = models.IntegerField()
    state = models.IntegerField()
    isdelete = models.IntegerField(null=True, blank=True)
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_talent'

class UserTemplate(models.Model):
    user_template_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    template_id = models.IntegerField()
    state = models.IntegerField()
    publish_date = models.DateTimeField()
    class Meta:
        db_table = u'user_template'

