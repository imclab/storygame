from django.shortcuts import get_object_or_404, render
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.models import get_current_site
from storygame.stories.models import Story, Membership, Line
from storygame.stories.forms import LineForm

# Create your views here.
def write(request, slug_story, activation_key, t='stories/write.html', d={}):
    story = get_object_or_404(Story, slug=slug_story)
    active_membership = story.active_membership()
    d['story']=story
    if not active_membership:
        story.turn_membership()
        return render(request, 'stories/done.html', d)
    membership = get_object_or_404(Membership, activation_key=activation_key)
    if active_membership.id != membership.id:
        return render(request, 'stories/done.html', d)
    new_line = Line(story=story)
    if request.POST:
        line_form=LineForm(request.POST, prefix='line', instance=new_line)
        if line_form.is_valid():
            line_form.save()
            next = story.turn_membership()
            mail_d = {
                'story': story,
                'site': get_current_site(request)
            }
            message = render_to_string('stories/email.txt', mail_d)
            email = EmailMessage(
                'Estas participando del concurso',
                message,
                to=[active_membership.user.email])
            email.send()
            return render(request, 'stories/done.html', d)  
    else:
        line_form=LineForm(prefix='line')
    d = {
        'form': line_form,
        'story': story,
        'site': get_current_site(request)
    }
    return render(request, t, d)

def detail(request, slug_story):
    pass
