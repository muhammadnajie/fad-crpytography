import re, os

def to_file(filename, msg):
    with open(filename, "w") as f:
        try:
            f.write(msg)
            return f"Successfully writing message to {os.path.abspath(filename)}"
        except:
            return "Failed to writing to the file."

def customize_text(type, source_text, target_text):
    if target_text == None:
        return "Incorrect type"
    return f"{type}({source_text}) = {target_text}"

def is_valid(text):
    return re.match(r"[a-z]+", text)