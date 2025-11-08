def is_admin(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_librarian(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

def is_member(user):
  return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'member'
