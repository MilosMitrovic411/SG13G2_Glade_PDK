# SG13G2_Glade_PDK
THIS PDK CONTAINS FILES MENT TO ENABLE SG13G2 TECHNOLOGY DESIGN IN GLADE.\
THE IHP'S OFFICAL PAGE FOR THE TECHNOLOGY AND GLADE HOME PAGES ARE LINKED BELLOW:\
https://www.ihp-microelectronics.com/services/research-and-prototyping-service/fast-design-enablement/open-source-pdk
https://peardrop.co.uk/

MAKE SURE TO DOWNLOAD THE LATEST VERSION OF GLADE BUILD, OTHERWISE SOME FEATURES WONT BE FUNCTIONAL.

TO USE PCELLS, YOU WILL HAVE TO ADD A PATH TO THE PCELLS FOLDER TO YOUR PYTHONPATH ENVIRONMENT VARIABLE.

IF YOU ARE USING WINDOWS, YOU CAN START GLADE USING A BATCH FILE PROVIDED, IN WHICH CASE, YOU WILL NEED TO PUT THE GLADE ADRESS WHERE GLADE_HOME IS.\
E.G. GLADE_HOME=C:\glade6_win64

ASLO, AFTER CREATING YOUR OWN LIBRARY, IF IT IS LOCATED WHITIN THIS FOLDER, YOU CAN INCLUDE IT IN galde_init.py FILE.\
E.G. mylibs = ["Cells", "MYLIB"]

ONE MORE USEFUL LIBRARY THAT YOU CAN ADD TO THE galde_init.py IS SPICE3LIB. IT CONTAINS MODELS USEFUL FOR DESIGN TESTING.\
SPICE3LIB IS INCLUDED IN APDKCNM25, WHICH YOU CAN FIND IN THE FOLLOWING LINK: https://www.cnm.es/users/pserra/apdk/download.html

THIS PDK WAS DEVELOPED ON WINDOWS, SO I DON'T KNOW IF THERE IS GOING TO BE ANY PORBLEMS WITH LINUX OR MAC USERS.\
IF THERE ARE ANY PLEASE RAISE AN ISSUE.

IN THIS PDK I HAVE ALSO INCLUDED DOCUMENTATION FROM THE ORIGINAL SG13G2 PDK AND AFTER TESTING I AM GOING TO, PROBABLY, INCLUDE THE ORIGINAL XYCE MODELS.\
I DO NOT OWN THESE, AND I DID NOT CONTRIBUTE TO THEIR CREATION, I AM JUST REDISTRIBUTING THEM UNDER THE TEARMS OF APACHE LICENCE 2.0.

THE CONTENTS OF THIS PDK ARE SUBJECT TO CHANGE.\
THERE MAY BE MORE CELLS ADDED, AND THERE MAY BE IMRPOVEMENTS TO ALREADY EXISTING ONES.\

MILOŠ MITROVIĆ
