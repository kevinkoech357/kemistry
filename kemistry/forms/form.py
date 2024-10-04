from flask_security.forms import RegisterForm
from wtforms.validators import DataRequired, Regexp, Email
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField
from wtforms import ValidationError


def validate_min_words(form, field):
    """
    Custom validator to check if content has a minimum of 500 words.
    """
    min_words = 300
    content = field.data.strip()
    words_count = len(content.split())
    if words_count < min_words:
        raise ValidationError(f"Content must have at least {min_words} words.")


class ExtendedRegisterForm(RegisterForm):
    """
    Extended registration form for users.

    Inherits from Flask-Security's RegisterForm.
    Adds additional fields for first name, last name,
    university, and qualification.
    """

    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(message="First name is required."),
            Regexp(r"^\S+$", message="First name cannot contain spaces."),
        ],
    )
    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(message="Last name is required"),
            Regexp(r"^\S+$", message="Last name cannot contain spaces."),
        ],
    )
    university = StringField(
        "University", validators=[DataRequired(message="University is required")]
    )
    qualification = SelectField(
        "Qualification",
        choices=[
            ("Diploma", "Diploma"),
            ("Undergraduate", "Associates Degree"),
            ("Bachelors Degree", "Bachelors Degree"),
            ("Postgraduate Diploma", "Postgraduate Diploma"),
            ("Masters Degree", "Masters Degree"),
            ("PhD", "PhD"),
        ],
        validators=[DataRequired(message="Qualification is required")],
    )

    def validate_on_submit(self):
        """
        Validate form data.

        Overrides FlaskForm's validate_on_submit method to customize behavior.
        Capitalizes the first letter of first_name, last_name, and university.

        Returns:
            bool: True if form data is valid, False otherwise.
        """
        if not super().validate_on_submit():
            return False

        # Capitalize the first letter of first_name, last_name, and university
        self.first_name.data = self.first_name.data.title()
        self.last_name.data = self.last_name.data.title()
        self.university.data = self.university.data.title()

        return True


class ContactForm(FlaskForm):
    """
    Form for contacting the site administrator.

    Inherits from Flask-WTF's FlaskForm.
    Includes fields for name, email, and message.
    """

    name = StringField(
        "Your Name", validators=[DataRequired(message="Name is required.")]
    )
    email = StringField(
        "Email Address",
        validators=[DataRequired(message="Valid email is required."), Email()],
    )
    message = TextAreaField(
        "Message", validators=[DataRequired(message="Message is required.")]
    )
    submit = SubmitField("Submit")


class BlogPostForm(FlaskForm):
    """
    Form for creating a new blog post.

    Inherits from Flask-WTF's FlaskForm.
    Includes fields for content, and an optional picture.
    """

    title = StringField("Title", validators=[DataRequired(message="Title is required")])
    content = TextAreaField(
        "Content",
        validators=[DataRequired(message="Content is required."), validate_min_words],
    )
    tag_choices = [
        ("organic", "Organic Chemistry"),
        ("physical", "Physical Chemistry"),
        ("inorganic", "Inorganic Chemistry"),
        ("general", "General Chemistry"),
        ("medicinal", "Medicinal Chemistry"),
    ]
    tag = SelectField(
        "Tag", choices=tag_choices, validators=[DataRequired(message="Tag is required")]
    )
    submit = SubmitField("Publish")


class CommentForm(FlaskForm):
    """
    Form for users to leave comments under
    posts if they resonate with the post or have a question
    or suggestion.
    """

    name = StringField(
        "Your Name", validators=[DataRequired(message="Name is required.")]
    )
    email = StringField(
        "Email Address",
        validators=[DataRequired(message="Valid email is required."), Email()],
    )
    message = TextAreaField(
        "Message", validators=[DataRequired(message="Message is required.")]
    )
    comment = SubmitField("Comment")


class EditBlogPostForm(FlaskForm):
    """
    Form for editing a new blog post.

    Inherits from Flask-WTF's FlaskForm.
    Includes fields for content, and an optional picture.
    """

    title = StringField("Title", validators=[DataRequired(message="Title is required")])
    content = TextAreaField(
        "Content",
        validators=[DataRequired(message="Content is required."), validate_min_words],
    )
    picture = FileField("Blog Picture")
    submit = SubmitField("Publish")


class EditProfileForm(FlaskForm):
    """
    Form for users to edit their profile details.

    Rendered by /settings route.
    """

    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    university = StringField("University", validators=[DataRequired()])
    qualification = SelectField(
        "Qualification",
        choices=[
            ("Diploma", "Diploma"),
            ("Associates Degree", "Associates Degree"),
            ("Bachelors Degree", "Bachelors Degree"),
            ("Postgraduate Diploma", "Postgraduate Diploma"),
            ("Masters Degree", "Masters Degree"),
            ("PhD", "PhD"),
        ],
        validators=[DataRequired(message="Qualification is required")],
    )
    bio = StringField("Bio", validators=[DataRequired()])
    submit = SubmitField("Save Changes")


class RecoverAccountForm(FlaskForm):
    """
    Form for recovering a suspended account.

    Inherits from FlaskForm and contains an email field.
    """

    email = StringField("Email", validators=[Email(), DataRequired()])
    submit = SubmitField("Recover Account")
