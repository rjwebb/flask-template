from . import app

@app.template_filter('example')
def example_filter(context):
    """
    This is an example jinja2 filter, it doesn't really do anything.
    """

    return context
