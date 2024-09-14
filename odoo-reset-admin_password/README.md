# Guide on How to Change the Admin Odoo Password in Case of Forgotten or Lost Admin Password

This simple Python script prompts the user to enter a password and returns the hashed (encrypted) version using the `passlib` library.

## Features
- Secure password hashing using the `pbkdf2_sha512` algorithm.
- 600,000 rounds of hashing to ensure high security.
- Easy to use and modify for other password encryption needs.

## Requirements
- Python 3.x
- `passlib` library

## Installation

To use this script, you need to install the `passlib` library. You can do so using `pip`:

```bash
pip install passlib

```

```markdown
## Step 2: Connect to PostgreSQL

### For Non-Docker Users:

1. **Connect to PostgreSQL:** To connect to the PostgreSQL server, use the following command in your terminal or command line:
   
   ```bash
   psql -h <hostname> -U <username>
   ```
   
   Replace `<hostname>` with your PostgreSQL host (e.g., localhost if running locally) and `<username>` with your PostgreSQL user account.

2. **Select the Odoo database:** Once connected to PostgreSQL, switch to the Odoo database you want to modify by using the following command:
   
   ```sql
   \c <database_name>;
   ```
   
   Replace `<database_name>` with the name of your Odoo database.

3. **Update the password:** Run this SQL query to update the password for the admin user:
   
   ```sql
   UPDATE res_users
   SET password = '<password_hash>'
   WHERE login = 'adminuser@example.com';
   ```

   Replace `<password_hash>` with the password you generated in Step 1.
   Replace `'adminuser@example.com'` with the actual login or email of the admin user in your Odoo database.

4. **Exit PostgreSQL:** Once the password has been updated, exit PostgreSQL by typing:
   
   ```bash
   \q
   ```

### For Docker Users:

If you are using Docker to manage PostgreSQL, follow these additional steps to access the database.

1. **Connect to your PostgreSQL container:** First, you need to enter the Docker container running PostgreSQL:
   
   ```bash
   docker exec -it <container_name> bash
   ```
   
   Replace `<container_name>` with the name of your PostgreSQL container.

2. **Access PostgreSQL inside the container:** Once inside the container, use the following command to connect to PostgreSQL:
   
   ```bash
   psql -d <hostname>  -U <username>
   ```
   
   Replace `<username>` with your PostgreSQL username.

3. **Select the Odoo database:** Just like with non-Docker users, switch to the Odoo database by running:
   
   ```sql
   \c <database_name>;
   ```

4. **Update the admin password:** Run the same SQL query as in the non-Docker example:
   
   ```sql
   UPDATE res_users
   SET password = '<password_hash>'
   WHERE login = 'adminuser@example.com';
   ```

   Replace `<password_hash>` with the hashed password generated in Step 1.
   Replace `'adminuser@example.com'` with the correct login or email of the admin user.

5. **Exit the container:** Once done, exit the PostgreSQL terminal by typing `\q` and then exit the container with:
   
   ```bash
   exit
   ```

