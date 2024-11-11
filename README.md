
## Installations

1. **Create a Virtual Environment:**
    - Use any of the following commands:
    ```sh
    python -m venv env

    # or

    python3 -m venv env
    ```

2. **Activate the Virtual Environment:**
    - On Linux/MacOS:
    ```sh
    source env/bin/activate
    ```
    - On Windows:
    ```sh
    env\Scripts\activate
    ```
3. **Database Setup:**
- Create a new postgres database and add the credentials in the the `.env` file as shown in `.env.example` file.

4. **Install the Requirements:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Move to the `src` Directory:**
    ```sh
    cd src
    ```

6. **Run Migrations:**
    - Apply the database migrations with the following command:
    
    ```sh
    python manage.py migrate
    ```

7. **Start the Server:**
    ```sh
    python manage.py runserver
    ```
