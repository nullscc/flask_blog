from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Tag

@main.app_context_processor
def inject_tag_model():
    return dict(Tag=Tag)