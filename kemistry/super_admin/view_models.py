from flask_admin.contrib.sqla import ModelView
from flask_security import current_user, url_for_security
from flask import abort, request, redirect


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

    can_delete = True
    can_create = False
    can_edit = True
    column_list = ["id", "username", "email", "created_at"]
    column_searchable_list = ["username", "email"]
    column_filters = ["active"]


class PostView(Permission):
    """
    Customized Flask-Admin view for the Post model.
    """

    can_delete = True
    column_list = ["id", "user_id", "title", "content", "created_at"]
    column_searchable_list = ["title", "content"]
    form_columns = ["user_id", "title", "content"]


class CommentView(Permission):
    """
    Customized Flask-Admin view for the Comments model.
    """

    can_delete = True
    column_list = ["id", "post_id", "name", "email", "message"]
    column_searchable_list = ["name", "email"]
    form_columns = ["post_id", "name", "email", "message"]
