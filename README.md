# Deploying a Bank Note Authentication model using FastAPI, on Heroku
## This problem is part of Kaggle: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data
### The objective of the problem is to distinguish between forged bank notes and authentic notes. The data comprises of 4 features and 1 target columns, and then create a Flask App which can be invoked via localhost/POSTMAN/Heroku.

#### The features are: 'variance', 'skewness', 'kurtosis', and 'entropy'. The target column is labelled as 'class'.

The features were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera, usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object, gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

This is a simple classification problem without much requirement for feature engineering. With a default RandomForest Classifier model, we were able to achieve >99% validation accuracy. The trained model is then saved as a .pkl file (classifier.pkl) for later use.

In traditional scenario, when we directly invoke the FastAPI app using uvicorn locally, we used to execute on CLI uvicorn.run(app, host='127.0.0.1', port=8000) which instructs that uvicorn should run the app.py file on host:127.0.0.1 and on port:8000. This app file, was similar to the Flask app we had created earlier, only in this case it was built using FastAPI and invoked using uvicorn (a ASGI server, different from the typical WSGI Flask server) will load the necessary method of the FastAPI app. We will finally use OpenAPI/Swagger for rendering a proper web-api interface, but it is also possible to invoke this FastAPI app locally. In the former case, we used http://127.0.0.1:8000/docs while for the latter we used either http://127.0.0.1:8000/ or http://127.0.0.1:8000/predict (for invoking either 2 defined methods of root (/) and (/predict) )or by simply using or http://127.0.0.1:8000/predict?variance=2&skewness=3&curtosis=2&entropy=1. The /predict is used to invoke the saved classification model for prediction. If defined a function predict_banknote, which leverages a pydantic library based class BankNote, for accepting user-input in a .json format, and passes these values to the classification model for prediction.

Now to run this on a Heroku like cloud based service, we needed to provide some additional changes. These were:
1. Procfile: 			This was similar to our earlier procfile that we were using for Flask based web-app, but the commands are changed to below:
						web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
							web: Is specific to procfile and is a command convention that helps identify the Heroku deployment process to start a 		web-application, as per the next command. 
							gunicorn: is the WSGI server on which we are configuring to run our application,with the below parameters:
							w 4: indicates that we need our application to run on gunicorn with 4 worker processes
							k uvicorn.workers.UvicornWorker tells gunicorn to run the application using uvicorn.workers.UvicornWorker class
							app: app specifies the app.py file where our FastAPI app is initialized
2. requirements.txt: 	This is once again similar to what we have used earlier with Heroku, only additionally this time we need to specify installation for uvicorn, gunicorn, fastapi, uvloop, and fastloops.

The deployment process is standard involving uploading the code to GitHub and then linking the same code-base to Heroku for it to do the needful for deployment.

The web-app is available at: https://deb-banknoteauth-fastapi.herokuapp.com/docs
