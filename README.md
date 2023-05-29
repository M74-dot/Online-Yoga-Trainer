# ONLINE YOGA TRAINER WEB APPLICATION

## How to run this application

### Python version required : Python 3.9.6 or greater

### firstly clone the repository
> git clone https://github.com/M74-dot/Online-Yoga-Trainer.git

### Run requirements.txt file to get all modules installed
> pip install -r requirements.txt

### Run the application
> streamlit run app.py

### If after executing above command its saying that module not found you can install that module using command
> pip install <module_name>

### It will run on some port 

### If want to run without sound simply comment out below lines of code from main.py file which is defined inside compare_pose function.
``` # Add text-to-speech conversion for this condition
        engine = pyttsx3.init()
        engine.say("Extend the right arm at elbow")
        engine.runAndWait()
        time.sleep(5)
         # Check for keyboard input to stop text-to-speech
        key = cv2.waitKey(10)
        if key == ord('q'):
            engine.stop()
```

THANK YOU!