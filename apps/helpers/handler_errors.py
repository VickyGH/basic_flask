from apps.helpers.message.error import ERROR_CODE_500, ERROR_MSG_500


class HandlerErrors:
    @staticmethod
    def handler_middleware_errors(error: Exception):
        code_error = ERROR_CODE_500
        message = ERROR_MSG_500