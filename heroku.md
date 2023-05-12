## Heroku

Before deploying to Heroku you should be familiar with the basic concepts of [Git](https://git-scm.com/) and [Heroku](https://heroku.com/).

If you keep your project on GitHub you can use 'Deploy to Heroku' button thanks to which the deployment can be done in web browser with minimal configuration required.
The configuration used by the button is stored in `app.json` file.

<a href="https://heroku.com/deploy" style="display: block"><img src="https://www.herokucdn.com/deploy/button.svg" title="Deploy" alt="Deploy"></a>
    <br>

Deployment by using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):

* Create Heroku App. You can leave your app name, change it, or leave it blank (random name will be generated)

    ```bash
    heroku create onlyonecode
    ```

* Add buildpacks

    ```bash
    heroku buildpacks:add --index=1 heroku/nodejs
    heroku buildpacks:add --index=1 heroku/python
    ```

* Set environmental variables (change `SECRET_KEY` value)

    ```bash
    heroku config:set SECRET_KEY=not-so-secret
    heroku config:set FLASK_APP=autoapp.py
    heroku config:set SEND_FILE_MAX_AGE_DEFAULT=31556926
    ```

* Please check `.env.example` to see which environmental variables are used in the project and also need to be set.

* Deploy on Heroku by pushing to the `heroku` branch

    ```bash
    git push heroku main
    ```
