from flask import Blueprint, render_template, redirect, url_for, flash, request
from kemistry.forms.form import ContactForm
from kemistry.models.post import Post
from kemistry.models.user import User
from flask_security import current_user, auth_required, url_for_security
import json


user = Blueprint("user1", __name__)


@user.route("/", methods=["GET"])
def home():
    """
    Render the homepage with all published blog posts.

    Returns:
        A rendered template of the homepage.
    """
    page = request.args.get("page", 1, type=int)

    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=12)

    total_posts = Post.query.count()

    return render_template("index.html", posts=posts, total_posts=total_posts)


@user.route("/profile")
@auth_required()
def profile():
    """
    Render the profile with the current user's
    profile image, bio, qualifications, and all the posts they have ever written.

    Returns:
        A rendered template of the profile.
    """
    # Retrieve the current user's information
    # If user is anonymous, request login
    user = current_user

    if not user:
        return redirect(url_for_security("login"))

    # Retrieve all posts written by the current user
    posts = Post.query.filter_by(author=user).all()

    return render_template("profile.html", user=user, posts=posts)


@user.route("/settings")
def settings():
    """
    Render the settins page.
    """
    return render_template("settings.html")


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
