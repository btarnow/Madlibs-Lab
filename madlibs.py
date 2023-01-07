"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page. <a href='/hello'>Submit a Greeting</a> "


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Get the users response and show accordingly"""

    response = request.args.get("play")
    if response == "yes":
        #continue with game rendered page (game.html)
        return render_template("game.html")
    else:
        #good by for variable (goodbye.html)
        return render_template("goodbye.html")
        

@app.route("/madlib")
def show_madlib():
#get request here
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("madlib_person")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    
    items = []
    items.append(request.args.get("item1"))
    items.append(request.args.get("item2"))
    items.append(request.args.get("item3"))
    print("This is items after append:")
    print(items)
    items = [x in items if isinstance(x, str)]
    # for loop through items
    # look at item x==index iteration
    # if 
    
    items=",".join(items)
    print("This is items after join:")
    print(items)
#variable name assigned
#ensure variable names match template
    return render_template("madlib.html", color = color.lower(), noun = noun, 
    person = person.title(), adjective = adjective.lower(), verb = verb, items = items)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
