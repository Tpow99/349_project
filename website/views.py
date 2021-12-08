from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from.models import UserData
from . import db
from .models import UserData
import pandas as pd
import requests         # grab web-page
from bs4 import BeautifulSoup as bsopa  # parse web-page
import datetime         # format date/time
import csv
from .auth import auth


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        job_field = request.form.get('job_field')
        location = request.form.get('location')
        salary = request.form.__getitem__('salary')
        print(job_field,location, salary)
        return render_template("results.html", user=current_user)
    else:
        return render_template("home.html", user=current_user)








