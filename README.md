# XO Anime - Local

This package allows you to watch your favorite anime locally without the need for deployment, ads, or login.

## Installation

1. Create a directory named `anime`.

mkdir anime

2. Navigate to the `anime` directory.

cd anime

3. Clone the API repository.

   - git clone https://github.com/consumet/api.consumet.org.git api

4. Clone the frontend repository.

   - git clone https://github.com/code-kasha/anime.git frontend

### If you use poetry

1. Navigate to the `frontend` directory. frontend/frontend

cd frontend

2. Install dependencies using Poetry.

poetry install

3. Apply database migrations.

python manage.py migrate

4. Start the server.

python manage.py runserver

### Using venv / virtualenv

1. Navigate to the `frontend` directory. "frontend/frontend"

cd frontend

2. Initialize a virtual environment (venv).

python3 -m venv env / virtualenv env

3. Activate the virtual environment.

source env/bin/activate

4. Install Django and requests using pip.

pip install django requests

5. Apply database migrations.

python manage.py migrate

6. Start the server.

python manage.py runserver

### Npm

1. Navigate to the `api` directory.

cd api

2. Install dependencies using npm.

npm install

3. Start the server.

npm start

### Yarn

1. Navigate to the `api` directory.

cd api

2. Remove the `package-lock.json` file.

rm package-lock.json

3. Install dependencies using yarn.

yarn install

4. Start the server.

yarn start

You will need two terminal windows, one for running the API and another for the frontend.

Once done, you can access the application by going to `localhost:8000` in your web browser.

Thank you for using XO Anime - Local!. Enjoy watching your favorite anime!

Also, I haven't used any css in the project. This is intentionally done to save time, I only follow a handful of series,
so few episodes per week. This actually works for me better than using anime sites. No data collection, no ads and the
instance is local. :D
