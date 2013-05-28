Image decision study
====================

![Screenshot](/screenshots/screenshot_1.png "Screenshot")

License
-------
Apache License, Version 2.0

Dependencies
-------
  - Django 1.3.5 (tested on pythonanywhere.com)
  - jQuery 1.9.1
  - [jQuery Cycle Plugin] [jQueryCycle] 2.9999.81 
  
Required configuration
-------
  - In ```urls.py``` add:

    url(r'^experiment/', include('website.experiment.urls'))
    
  - In ```settings.py``` set ```IMAGES_PATH``` to the base URL for images.

 

  [jQueryCycle]: http://jquery.malsup.com/cycle/