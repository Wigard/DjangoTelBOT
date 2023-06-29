from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .tgbot import sendMessage_1, sendMessage_2
from .models import autoMessageItem

# Create your views here.
def tgbot(request):
  textItem = autoMessageItem.objects.all().values()
  template = loader.get_template('tgbot.html')
  context = {
    'textItem': textItem,
  }
  return HttpResponse(template.render(context, request))

def test(request, id):
    textItem = autoMessageItem.objects.get(id=id)
    template = loader.get_template('result.html')
    context = {
      'textItem': textItem,
      'link_1': sendMessage_1,
      'link_2': sendMessage_2
    }
    return HttpResponse(template.render(context, request))