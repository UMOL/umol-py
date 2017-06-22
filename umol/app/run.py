from .catalog import catalog

def run(app: str, argd: dict):
    c = catalog()
    if app in c.keys():
        return c[app](argd)
    else:
        return "\n".join(
            [
                "Error hint: app {} is not available.",
                "   Check your spelling",
            ]
        )
