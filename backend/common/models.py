from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class BaseModel(SafeDeleteModel):
    """
    Attributes for all model data
    """
    _safedelete_policy = SOFT_DELETE
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True