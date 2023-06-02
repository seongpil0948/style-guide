from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from app.models.poly import Project, ArtProject, ResearchProject

@admin.register(Project)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Project  # Optional, explicitly set here.
    child_models = (ArtProject, ResearchProject)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.

class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Project  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    base_form = ...
    base_fieldsets = (
        ...
    )


@admin.register(ArtProject)
class ModelBAdmin(ModelAChildAdmin):
    base_model = ArtProject  # Explicitly set here!
    # define custom features here


@admin.register(ResearchProject)
class ModelCAdmin(ModelBAdmin):
    base_model = ResearchProject  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site
    # define custom features here





