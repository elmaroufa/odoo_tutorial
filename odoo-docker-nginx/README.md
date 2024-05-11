# odoo-17-docker

the folder nginx content odoo.conf for ngnix

## Config nginx

- Create/Edit the file odoo.conf for nginx (if your system is ubuntu)
  
  ```
   sudo nano /etc/nginx/sites-available/odoo.conf
  ```
  
- Edit file (odoo.conf) using link documentation or see folder nginx/odoo.conf
  
   ```
  https://www.odoo.com/documentation/17.0/administration/on_premise/deploy.html
  ```
   ## NB: Attention, in the documentation, the odoo.conf configuration file is presented in the "/etc/nginx/sites-enabled/odoo.conf" directory. It is preferable to create it in "site-available" and create a symbolic link.
   
- Enable the Nginx Configuration by Creating a Symbolic Link in the "/etc/nginx/sites-enabled" 
  
   ```
   sudo ln -s /etc/nginx/sites-available/odoo.conf /etc/nginx/sites-enabled/
  ```
- Verify the Nginx Configuration:

   ```
    sudo nginx -t
  ```
  
- Reload Nginx to Apply the New Configuration:

  ```
     sudo systemctl reload nginx.service

  ```
  
  ## Star odoo server and using bash

  - stard odoo using docker compose
    
     ```
     docker compose up -d
     ```
     
  - Using odoo-bin in container:

     ```
     docker exec -it <container_name>  bash
     ```
  - Update database and module

    ```
    odoo --addons-path=/mnt/addons -d <dbname> -u <module> 
    ```
  
  - Run unit tests on Docker
   
    ```
    odoo --addons-path=/mnt/addons -d <dbname> -u <module> --log-level=test --test-enable --stop-after-init
    ```
  
