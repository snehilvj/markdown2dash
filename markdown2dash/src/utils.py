def create_heading_id(text):
    return "-".join(text.lower().split())


def create_class_name(text):
    return "-".join(text.lower().split("_"))
