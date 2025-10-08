# Central wiring/factory for app components
# Call init_app(app) early in app startup to construct DB/DAOs and managers.

from typing import Optional

# module-level singletons populated by init_app
dao = None
user_manager = None
book_manager = None
admin_manager = None


def init_app(app):
    """Initialize DAOs and managers using the provided Flask app.
    This function must be called before importing route modules that rely on managers.
    """
    global dao, user_manager, book_manager, admin_manager

    # Import DAO implementation and create instance
    from Models.DAO import DAO as DAOClass
    dao = DAOClass(app)

    # Import controller classes and instantiate them with the DAO
    from Controllers.UserManager import UserManager
    from Controllers.BookManager import BookManager
    from Controllers.AdminManager import AdminManager

    user_manager = UserManager(dao)
    book_manager = BookManager(dao)
    admin_manager = AdminManager(dao)

    # expose for convenience
    return {
        'dao': dao,
        'user_manager': user_manager,
        'book_manager': book_manager,
        'admin_manager': admin_manager,
    }
