from django.http import HttpResponse
from django.template import loader
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Посещена главная страница')
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    logger.info('Посещена страница "Обо мне"')
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
