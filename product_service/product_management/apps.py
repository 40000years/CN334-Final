import os
import logging
from django.apps import AppConfig
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class ProductManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_management'

    def ready(self):
        # รันเฉพาะใน main process (ไม่รันใน worker หรือ migration)
        if os.environ.get('RUN_MAIN', None) != 'true':
            return
        try:
            User = get_user_model()
            username = os.getenv("ADMIN_USERNAME", "admin")
            password = os.getenv("ADMIN_PASSWORD", "Admin123!")
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, "", password)
                logger.info(f"Created superuser: {username}")
            else:
                logger.info(f"Superuser {username} already exists")
        except Exception as e:
            logger.error(f"Error creating superuser: {e}")