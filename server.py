from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {}


@app.route("/")
def main_page():
    return render_template("main.html", tasks=tasks)


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        if len(tasks) != 0:
            tasks.update({max(tasks.keys())+1: request.form['new-task']})
        else:
            tasks.update({0: request.form['new-task']})
    return redirect("/")


@app.route("/remove-task", methods=["GET", "POST"])
def remove_task():
    if request.method == "POST":
        tasks.pop(int(request.args.get('task-to-remove')))
    return redirect("/")


if __name__ == '__main__':
    app.run(
        debug=True
    )
