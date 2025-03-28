from django.db import models

# tickets
TICKET_TYPES = (
    ("author_create_curation", "Author create curation"),
    ("author_create_user", "Author create user"),
    ("author_update_curation", "Author update curation"),
)
DEFAULT_TICKET_TYPE = "author_create_curation"

# workflows


class StatusChoices(models.TextChoices):
    RUNNING = "running", "Running"
    APPROVAL = "approval", "Waiting for approval"
    PROCESSING = "processing", "Processing"
    COMPLETED = "completed", "Completed"
    ERROR = "error", "Error"


DEFAULT_STATUS_CHOICE = StatusChoices.PROCESSING


class WorkflowType(models.TextChoices):
    HEP_CREATE = "HEP_CREATE", "HEP create"
    HEP_UPDATE = "HEP_UPDATE", "HEP update"
    AUTHOR_CREATE = "AUTHOR_CREATE", "Author create"
    AUTHOR_UPDATE = "AUTHOR_UPDATE", "Author update"


DEFAULT_WORKFLOW_TYPE = WorkflowType.HEP_CREATE

allowed_workflow_types = [
    WorkflowType.AUTHOR_CREATE,
    WorkflowType.AUTHOR_UPDATE,
]


class AuthorResolutionDags(models.TextChoices):
    accept = "accept", "author_create_approved_dag"
    reject = "reject", "author_create_rejected_dag"
    accept_curate = "accept_curate", "author_create_approved_dag"


DECISION_CHOICES = AuthorResolutionDags.choices


class AuthorCreateDags(models.TextChoices):
    initialize = "author_create_initialization_dag", "initialize"
    approve = "author_create_approved_dag", "approve"
    reject = "author_create_rejected_dag", "reject"


class AuthorUpdateDags(models.TextChoices):
    initialize = "author_update_dag", "initialize"


WORKFLOW_DAGS = {
    WorkflowType.HEP_CREATE: "",
    WorkflowType.HEP_UPDATE: "",
    WorkflowType.AUTHOR_CREATE: AuthorCreateDags,
    WorkflowType.AUTHOR_UPDATE: AuthorUpdateDags,
}
