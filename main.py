from website import create_app

# Creating an instance of our flask app 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Run the flask app with debugging
