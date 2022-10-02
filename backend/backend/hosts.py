from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    # host(r'api', 'api.urls', name='api'),
    # host(r'db-api-v2', 'api.urls', name='api'),
    # host(r'akwaabaclients', 'akwaaba_forms.urls', name='akwaaba_forms: CLIENTS'),
    # host(r'akwaabaapp', 'akwaaba_forms_public.urls', name='akwaaba_forms: PUBLIC'),
    # host(r'akwaabaadmin', 'django.contrib.admin.site.urls', name='akwaaba_forms: ADMIN'),
    host(r'systems-backend-admin', 'django.contrib.admin.site.urls', name='ADMIN'),
    # host(r'files', 'akwaaba_forms_public.urls', name='akwaaba_forms: FILES'),
)
# akwaaba
# akwaabaapi
# akwaabaclients
# akwaabaapp
# akwaabaadmin