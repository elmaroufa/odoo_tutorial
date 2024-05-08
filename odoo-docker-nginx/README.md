# odoo-17-docker

the folder nginx content odoo.conf for ngnix

## Config nginx

- Create/Edit the file odoo.conf for nginx (if your system is ubuntu)
  
  ```
   sudo nano /etc/nginx/sites-available/odoo.conf
  ```
  
- Edit file (odoo.conf) using link documentation
  
   ```
  https://www.odoo.com/documentation/17.0/administration/on_premise/deploy.html
  ```
   
- Enable the Nginx Configuration by Creating a Symbolic Link in the "/etc/nginx/sites-enabled" Directory:
  
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
  
- 
