import sys

def init_tracer():
    MODE = 2

    def tracer(frame, event, arg):
        if event != 'call':
            return

        co = frame.f_code
        func_name = co.co_name
        func_line_no = frame.f_lineno
        func_filename = co.co_filename
        caller = frame.f_back
        caller_name = caller.f_code.co_name
        caller_line_no = caller.f_lineno
        caller_filename = caller.f_code.co_filename

        if MODE == 2:
            if ("sentry_sdk" not in func_filename or
                "sentry_sdk" in func_filename and "sentry_sdk" in caller_filename):
                return

        print(f"Calling {func_filename}:{func_line_no} {func_name} from:")

        if MODE == 2:
            caller = frame
            for i in range(5):
                caller = caller.f_back
                caller_name = caller.f_code.co_name
                caller_line_no = caller.f_lineno
                caller_filename = caller.f_code.co_filename
                print(f"from {caller_filename}:{caller_line_no} {caller_name}")

            print("="*50)

        return

    from django.core.handlers.wsgi import WSGIHandler
    old_app = WSGIHandler.__call__

    def trace_patched_handler(self, environ, start_response):
        sys.settrace(tracer)
        rv = old_app(self, environ, start_response)
        sys.settrace(None)
        return rv

    WSGIHandler.__call__ = trace_patched_handler
