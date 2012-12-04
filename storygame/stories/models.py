import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.hashcompat import sha_constructor

class Story(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def active_membership(self):
        actives = self.memberships.filter(is_active=True)
        if actives.count() > 0:
            print actives[0]
            return actives[0]

    def turn_membership(self):
        next = self.memberships.filter(is_active=False).order_by('?')[0]
        old = self.active_membership()
        if old:
            old.deactivate()
        next.activate()
        return next

    def last_line(self):
        return self.lines.order_by('pk').reverse()[0]

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __unicode__(self):
        return self.name

class Line(models.Model):
    line = models.CharField(max_length=256)
    story = models.ForeignKey(Story, related_name='lines')

    def last_words(self):
        splited = self.line.split(' ')
        count = len(splited) if len(splited) < 6 else 6
        count = -1 * count
        return ' '.join(splited[count:])

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = 'Lines'

    def __unicode__(self):
        return "%s (%s)" % (self.story.name, self.pk)

class Membership(models.Model):
    story = models.ForeignKey(Story, related_name='memberships')
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=40, unique=True)

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        salt = sha_constructor(str(random.random())).hexdigest()[:5]
        username = self.user.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        self.activation_key = sha_constructor(salt+username).hexdigest()
        self.save()

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'
 
    def __unicode__(self):
        return "%s en %s" % (self.user.username, self.story.name)
      

    

