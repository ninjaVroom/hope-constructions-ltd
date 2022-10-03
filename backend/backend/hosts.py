from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    host(r'api', 'api.urls', name='api'),
    host(r'cms', 'backend.admin_url', name='ADMIN'),
)
# akwaaba
# akwaabaapi
# akwaabaclients
# akwaabaapp
# akwaabaadmin