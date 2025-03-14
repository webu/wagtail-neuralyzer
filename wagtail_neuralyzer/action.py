import logging

from django.core.exceptions import PermissionDenied

from wagtail.log_actions import log

logger = logging.getLogger("wagtail_neuralyzer")


class NeuralyzePermissionError(PermissionDenied):
    """
    Raised when the object unpublish cannot be performed due to insufficient permissions.
    """

    pass


class NeuralyzeAction:
    def __init__(self, object, commit=True, user=None, log_action=True, neuralyzer=None):
        self.object = object
        self.commit = commit
        self.user = user
        self.log_action = log_action
        self.neuralyzer = neuralyzer

    def check(self, skip_permission_checks=False):
        if (
            self.user
            and not skip_permission_checks
            and not self.object.permissions_for_user(self.user).can_neuralyze()
        ):
            raise NeuralyzePermissionError("You do not have permission to neuralyze this object")

    def _commit_neuralyze(self, object):
        object.save()

    def _after_neuralyze(self, object):
        pass
        # utilisé pour lancer un signal
        # neuralyzed.send(sender=type(object), instance=object)

    def _neuralyze_object(self, object, commit, user, log_action):
        """
        Neuralyze the object using Neuralyzer

        :param log_action: flag for logging the action. Pass False to skip logging. Can be passed an action string.
            Defaults to 'wagtail.neuralyze'
        """
        self.neuralyzer.run(filters={"pk": object.pk})

        if commit:
            self._commit_neuralyze(object)

        if log_action:
            log(
                instance=object,
                action=log_action
                if isinstance(log_action, str)
                else "wagtail_neuralyzer.neuralyze",
                user=user,
            )

        logger.info('Neuralyzed: "%s" pk=%s', str(object), str(object.pk))

        self._after_neuralyze(object)

    def execute(self, skip_permission_checks=False):
        self.check(skip_permission_checks=skip_permission_checks)

        self._neuralyze_object(
            self.object,
            commit=self.commit,
            user=self.user,
            log_action=self.log_action,
        )
