from flask_admin import BaseView, expose
from kemistry.models.user import User
from kemistry.models.post import Post
from kemistry.super_admin.view_models import Permission


class AnalyticsView(BaseView):
    """
    A Flask-Admin view for displaying analytics data.

    This view provides analytics data such as the total number of users
    and posts in the system. It queries the database for this information
    and renders it in the admin interface.
    """

    @expose("/")
    def index(self):
        """
        Render the analytics view.
        """
        total_users = User.query.count()
        total_posts = Post.query.count()

        return self.render(
            "admin/analytics.html", total_users=total_users, total_posts=total_posts
        )
