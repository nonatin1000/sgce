from django.contrib import admin
from sgce.certificates.models import Template, Certificate, Participant, CertificateHistory

admin.site.register(Template)
admin.site.register(Participant)
admin.site.register(Certificate)
admin.site.register(CertificateHistory)