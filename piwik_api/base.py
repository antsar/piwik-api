"""Abstract base classes."""

from functools import wraps


class BaseModule:

    """Abstract base class for API modules."""

    def __init__(self, pa):
        """Construct this object."""
        self.pa = pa

    def _preprocess(self, args):
        """Apply common transformations to API call arguments."""
        def preprocess_dates(args):
            """Combine date and end_date into a range."""
            if 'date' in args:
                if args.get('period') == 'range' and 'end_date' in args:
                    args['date'] = '{},{}'.format(args['date'],
                                                  args['end_date'])
            return args

        def preprocess_bools(args):
            """Convert all booleans to integers."""
            for arg in args:
                if type(args[arg]) == bool:
                    args[arg] = int(args[arg])
            return args
        for name, value in locals().items():
            if name.startswith('preprocess_') and callable(value):
                args = value(args)
        return args


def api_method(func):
    """Decorator for all API call methods."""
    @wraps(func)
    def decorator(self, return_request_args=False, *args, **kwargs):
        request_args = func(self, *args, **kwargs)
        request_args.update({
            'method': '{module}.{method}'.format(
                module=self.__class__.__name__,
                method=func.__name__)})
        request_args = self._preprocess(request_args)
        if return_request_args:
            return request_args
        else:
            return self.pa.request(**request_args)
    return decorator
