# pomf_expirey_support
Expirey support for nokonoko/pomf, nojs only

Steps to reproduce:

1.) Replace index.html (or whatever your nojs version is called) with my index.html

2.) Place the Python script in your /var/www/whatever_your_main_dir_is_called directory (this is for Apache2)

3.) Replace your upload.php file with mine

4.) Make sure your DB has the schema used here: https://github.com/nokonoko/Pomf/blob/master/schema.sql

5.) Type "crontab -e" in your shell, paste the line I have in the crontab file

7.) Enjoy
