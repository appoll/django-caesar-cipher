# django-caesar-cipher
Attempt to polish python skills by building a basic encryption django app.

This file is a deposit of all valuable lessons learned along the way

## Django notes ##
1.  *apps* are not *projects* are not *apps*  
The project structure following `django-admin startproject caesar` looks like this:
		
		# Renamable project container	
		caesar/	
			manage.py
			# Python package for the project
			# Contains settings for the project environment 
			caesar/ 
				__init__.py
				settings.py
				urls.py
				wsgi.py
**Note**: maybe the *project* shouldn't have been called *caesar* in the first place, but something more general. The actual caesar cipher implementation is part of an *app*, which is created with `python manage.py startapp caesarapp`, resulting in:

		# Renamable project container	
		caesar/	
			manage.py
			# Python package for the project
			# Contains settings for the project environment 
			caesar/ 
				__init__.py
				settings.py
				urls.py
				wsgi.py
			# Python package for the app
			caesarapp/
				__init__.py
				admin.py
				apps.py
				models.py
				tests.py
				views.py

**Note** *models.py* and *views.py* only exist in the *app* directory

[**source**](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)    
2. 

## Git notes ##
1. **when:** 

		$ git init 
        $ git remote add origin <url>
		# on master branch
		  
	**what:** 
		
		$ git pull
		"There is no tracking information for the current branch."
			
	**solved:**
		
		$ git pull <source-branch> <destination-branch>
			OR
		$ git branch --set-upstream-to = <source-branch> <master>	

	**Note:** branch tracking is set by default when *cloning*.

	[**source**](http://stackoverflow.com/a/32056416/1368705)
