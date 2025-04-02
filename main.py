"""A simple API to track writing."""

from flask import Flask, request

from entry_functions import load_all_entries, is_valid_entry, save_entry

api = Flask(__name__)


@api.get("/")
def index():
    return {"message": "Welcome!"}


@api.route("/entry", methods=["GET", "POST"])
def get_entry():
    if request.method == "GET":
        entries = load_all_entries
        args = request.args

        if "author" in args:
            author = args["author"]
            [e for e in entries if e["author"].lower() == author.lower()]

        return entries

    else:
        new_entry = request.json
        if is_valid_entry(new_entry):
            created_entry = save_entry(new_entry)
            return created_entry, 201
        else:
            return {"error": True, "message": "Invalid entry."}, 400


if __name__ == "__main__":
    api.run(port=8080, debug=True)
