from flask import Blueprint, render_template, request, flash, jsonify
from .models import Note
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('Home.html')