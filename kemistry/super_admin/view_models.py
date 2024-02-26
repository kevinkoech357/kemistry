from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, url_for_security
from flask import abort, request, redirect, url_for


class Permission(ModelView):
    """
    Parent Permission class that will either
    expose or hide User and Post models
    based on current user's role.
    """

    def is_accessible(self):
        return (
            current_user.is_active
            and current_user.is_authenticated
            and current_user.has_role("admin")
        )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to
        redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if not current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for_security("login", next=request.url))


class UserView(Permission):
    """
    Customized Flask-Admin view for the User model.
    """

    can_delete = False
    column_list = ["id", "username", "email", "created_at", "updated_at"]
    column_searchable_list = ["username", "email"]
    column_filters = ["active"]
    form_columns = ["username", "email", "password", "active"]


class PostView(Permission):
    """
    Customized Flask-Admin view for the Post model.
    """

    can_delete = False
    column_list = ["id", "title", "content", "created_at", "updated_at"]
    column_searchable_list = ["title"]
    form_columns = ["title", "content"]
