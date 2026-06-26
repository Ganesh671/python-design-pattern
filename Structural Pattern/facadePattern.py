# Facade is an outward appearance that is used to conceal a less pleasant or credible reality


import azure.functions as func

app = func.FunctionApp()

@app.route("hello")
def http_trigger(req):
    user = req.params.get("user")
    return f"Hello, {user}!"