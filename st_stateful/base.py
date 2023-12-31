def _on_change_factory(_state_function):
    """A wrapper to allow user-defined `function` but also update widget state.

    When called, it always fires `_state_function` with `_session`,`_key` args, needed to preserve widget state.
    """

    # Inspiration: https://www.artima.com/weblogs/viewpost.jsp?thread=240845#decorator-functions-with-decorator-arguments
    def decorator(function):
        def wrapper(*args, **kwargs):
            _state_function()
            return function(*args, **kwargs) if function else None

        return wrapper

    return decorator
