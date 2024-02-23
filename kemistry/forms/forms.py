from flask_security.forms import RegisterForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Regexp


class ExtendedRegisterForm(RegisterForm):
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
            ("diploma", "Diploma"),
            ("undergraduate", "Undergraduate"),
            ("postgraduate_diploma", "Postgraduate Diploma"),
            ("masters_degree", "Masters Degree"),
            ("phd", "PhD"),
        ],
        validators=[DataRequired(message="Qualification is required")],
    )

    def validate_on_submit(self):
        if not super().validate_on_submit():
            return False

        # Capitalize the first letter of first_name, last_name, and university
        self.first_name.data = self.first_name.data.title()
        self.last_name.data = self.last_name.data.title()
        self.university.data = self.university.data.title()

        return True
