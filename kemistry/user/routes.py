from flask import Blueprint, render_template, redirect, url_for, flash
from kemistry.forms.forms import ContactForm
import json
from datetime import datetime

user = Blueprint("user1", __name__)


@user.route("/", methods=["GET"])
@user.route("/home")
def home():
    """
    Render the homepage.

    Returns:
        A rendered template of the homepage.
    """
    return render_template("index.html")


@user.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Render the contact page and handle contact form submissions.

    GET:
        Renders the contact form.

    POST:
        Validates and processes the contact form data, saves it to a JSON file,
        and redirects the user to the homepage.

    Returns:
        For GET requests: A rendered template of the contact form.
        For POST requests: A redirect to the homepage after form submission.
    """
    form = ContactForm()

    if form.validate_on_submit():
        date = datetime.utcnow()
        form_data = {
            "name": form.name.data,
            "email": form.email.data,
            "message": form.message.data,
        }
        save_data_to_json(form_data)
        flash("Message sent successfully! We'll get back to you soon.", "success")
        return redirect(url_for("user1.home"))

    return render_template("contact.html", form=form)


def save_data_to_json(data):
    """
    Save contact form data to a JSON file.

    Args:
        data: A dictionary containing contact form data (name, email, message).

    Returns:
        None
    """
    try:
        with open("contact.json", "a") as json_file:
            json.dump(data, json_file, indent=3)
            json_file.write("\n")

    except Exception as e:
        print(f"Error saving data to JSON file: {str(e)}")
