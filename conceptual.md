### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    Python is generally a backend server side language and javascript is a front end language that runs in the browser

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    .get()
    .setdefault()

- What is a unit test?
    A unit test is a way to build and test your code

- What is an integration test?
    A test to check to see if your code work together

- What is the role of web application framework, like Flask?
    Make languages easier/faster to write 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
      The correct choice would depends if the url should be hard-coded or scalable 

- How do you collect data from a URL placeholder parameter using Flask?
    request.args.get()

- How do you collect data from the query string using Flask?
    request.args.get()

- How do you collect data from the body of the request using Flask?
    request.form[]

- What is a cookie and what kinds of things are they commonly used for?
    a cookie is a way to store data on a server similarly to session
- What is the session object in Flask?
    store data on a server that gets deleted when a user no longer is on or using the server

- What does Flask's `jsonify()` do?
    It turns the response into a json object
