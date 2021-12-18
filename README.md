# E-Store()

## Keys

1. [Setup](#setup)
2. [Build](#build)
3. [Installations](#installations)

<a href="setup"></a>
# Setup
To setup this project I followed the Boutique-Ado walkthrough project with Code Institute. Since the whole project is to create an e commerce store, I user the code institute walkthrough as a guide. Having said that I have not copied the Boutique-Ado walkthrough, I have just followed it loosely to ensure I hit all requirements for a passing grade for PP5. Any code that I have taken from Boutique-Ado will be credited appropriately.
To start this project, I first instelled Django and Django allauth. Then created a project called estore using the startproject command. Once that was done, I created a superuser, Ran the port 8000 server and checked everything was working correctly


<a href="build"></a>
# Bulid
There are several different app within the project. This was done to help keep the code from getting too cluttered and by keeping things in seperate apps depending on that they are being used for enabled me to find and solve any problems much easier. There is a file in the top level called templates, this is where the allauth templates are stored and where the project base.html file is stored. This file contains all of the content that needs to be spread across all of the webpages. This includes both the navigation bar and the footer.
The first app created was the home app. This is where all of the homepage content is stored. For the homepage there is a container with a small description enticing customers to click the shop now button that will take them to the store page.  
The navigation bar contains, the website name, categories, store, user's account and settings. User basked cost and a search bar for users to search for various items.  
<img src="./media/readme/homepage-1.png" alt="First view of homepage">

<a href="installations"></a>
# Installations
In order to complete this project, quite a few imports were needed, they are all listed below:  
[Python](https://www.python.org/)  
[Django](https://docs.djangoproject.com/en/4.0/)  
[Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)  



Photo by <a href="https://unsplash.com/@keithmisner?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Keith Misner</a> on <a href="https://unsplash.com/s/photos/background?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  