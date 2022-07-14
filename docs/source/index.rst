.. Sakatoon documentation master file, created by
   sphinx-quickstart on Thu Apr  7 16:26:13 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation index
===================

This is Les Fruits Défendus main documentation.

It includes documentation about the Saskatoon harvest management system
as well as pick-leaders harvest guides.

To download these guides as PDF, follow the links bellow: 
   
- `PDF (fr) <https://lesfruitsdefendus.readthedocs.io/_/downloads/fr/latest/pdf/>`_
- `PDF (en) <https://lesfruitsdefendus.readthedocs.io/_/downloads/en/latest/pdf/>`_


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   pre-pick-guide/index
   harvest-guide/index


What's new in Saskatoon 2022
----------------------------

The collective worked hard over the last two years to develop an updated version of Saskatoon.
We fixed many bugs and added a few improvements. 

Changes that affect pick-leaders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Les Fruits Défendus Guides are now accessible as a public website instead of being PDF documents.
  Note that the documentation is still a work in progress and the website will be updated during the season. 
- Saskatoon now sends mails from the following email address: lesfruitsdefendus@riseup.net, incoming emails will be redirected to info@lesfruitsdefendus.org.
- Unselected pickers receive an email when the harvest passes from status "Date Scheduled" to 'Ready". The template looks like the following::
   
   Hi {name}

   We are sorry but enough pickers have already been selected 
   for the {harvest}. You may still be contacted by the 
   pick-leader if some of them end up cancelling. 
   We will do our best to prioritize your participation 
   next time you submit a request re-using the same email for another harvest.

   Thanks for supporting your community!
   Yours

   --
   Saskatoon Harvest System
   
  Pick-leader still need to organize with selected pickers.


Changes that mostly affect core members
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- When a pending property has been validated, the tree owner receives a confirmation email. The template looks like the following::
  
   Hi {name}

   Your tree subscription has been validated 
   by a member of Les Fruits Défendus.
   A pick leader might contact you to plan a 
   harvest this season.

   Thanks for supporting your community!
   Yours

   --
   Saskatoon Harvest System

- The process to register new users has been enhanced such that an "Auth-User" is always created when using this new form: https://saskatoon.lesfruitsdefendus.org/person/create/.
  You will be asked to select role(s) for this new user. The roles determine the privileges of the user (see https://github.com/LesFruitsDefendus/saskatoon-ng/blob/develop/doc/permissions.org for more infos).
  Then, use the "Register User" button from the community page to create a password for this user.

- The process to validate new properties has been enhanced such that:
  
  - A list of similar properties is listed to help determine if the property already exist in database.
    Still double check by searching in the property list, though.
  - The pending email address is used to create a new person automatically when clicking on "Register"
  - For more information on the process, please read this ticket: https://github.com/LesFruitsDefendus/saskatoon-ng/issues/71#issue-876449595

More infos on Les Fruits Défendus
---------------------------------

- `www.lesfruitsdefendus.org <http://www.lesfruitsdefendus.org>`_ 
- `(514) 360-8566 <tel:+15143608566>`_
- `info@lesfruitsdefendus.org <mailto:info@lesfruitsdefendus.org>`_
- Santropol Roulant, 111 rue Roy est, Montréal (QC) H2W 1M1
