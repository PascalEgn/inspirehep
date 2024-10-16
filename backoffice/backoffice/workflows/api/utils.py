from backoffice.workflows.api import serializers


def add_decision(workflow_id, user, action):
    serializer_class = serializers.DecisionSerializer
    data = {"workflow": workflow_id, "user": user, "action": action}

    serializer = serializer_class(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return serializer.data


def render_validation_error_response(validation_errors):
    validation_errors_messages = [
        {
            "message": error.message,
            "path": list(error.path),
        }
        for error in validation_errors
    ]
    return validation_errors_messages
