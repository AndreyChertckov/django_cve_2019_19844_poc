from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="mike123"):
    User.objects.create_user('mike123', 'mike@example.org', 'test123')

