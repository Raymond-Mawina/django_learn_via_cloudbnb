http://syllabus.africacode.net/projects/django-airbnb-clone/intro/index.html

## feature branching

This might be the clearest description of feature branching in the known universe: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow

And here are a few more resources to help you understand.

https://bocoup.com/blog/git-workflow-walkthrough-feature-branches
https://www.atlassian.com/agile/software-development/branching
Some basic best practices
Always make sure you have pulled the latest master branch before making a new branch

Always make sure that your branch starts at the head of the master branch.

git checkout master
git pull
git checkout -b $YOUR_SENSIBLE_BRANCH_NAME
Always give your branches meaningful names. If you name your branch any variation of my branch or branch 1 then you might as well name it I am a complete noob.

Before making a pull request then make sure your branch is up to date with the latest master branch. This is especially important when working on a team because sometimes things get merged into master that conflict with your code. If there are conflicts your code will not get merged. Period.

The first thing you need to do here is pulling the latest master branch. Then you have 2 options:

This way is a plain old merge.

git checkout $YOUR_SENSIBLE_BRANCH_NAME
git merge master
Many professionals prefer a rebase. These are a little bit trickier to understand but are generally considered best practices.

git checkout $YOUR_SENSIBLE_BRANCH_NAME
git merge master
Also, please remember to push your code often. If you make a PR and your code on GitHub is out of date then that sucks. And if something bad happens to your computer it’s important to have a backup. git is your code backup.

Making user-friendly PRs
When you make a pull request, give it a good name.

If there is an issue or a description of what you are supposed to do then link to that. Otherwise, describe what you are trying to do.

If your PR includes code that makes a change to a user interface then it’s good to include a screenshot of the user interface. Sometimes it’s even good to include a short video demonstrating the feature you just added so that people can see what the code does without having to run everything.

## Django tutorial

Please go through the following tutorial.

Remember that when using Django you should be using modern Python. If you are using Pythhon2.7 that would be a problem.

To check your python version:

python --version
You should be using some version of Python 3. At time of writing Python3.8 is available.

You should also be using a virtual environment or similar to isolate your django application and its depedencies.

https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## Actual instructions

In this project we’ll be building out a simple version of Airbnb. By the end there will be a lot of cool functionality. But we’ll do it piece by piece.

Take a look at Airbnb if you haven’t already. https://www.airbnb.co.za/

End goal
By the end of this multi-part project we’ll need the following.

register
make bookings for specific dates
see stats about the properties they own
And we need to give superusers/staff access to a a few different things. But we’ll get into that a bit later :)

KISS
If you haven’t heard of the principle of KISS look it up now. Generally, when building a kick-ass and complicated piece of software, it’s very very important to focus on what is actually required.

Many undisciplined developers fall down all sorts of rabbit holes and just build out a lot of half-broken and fully-useless bells and whistles instead of focusing.

You should always aim to follow the leanest, most steamlined path. Start off by making sure you will ne sucessful in building the stuff that is actually required before you consider scope creep.

Never heard of scope creep? Look that up too.

Feature branching
Please follow best practices here.

Some notes on infrastructure
Please use a Postgres database. Run it in a docker container.

We use this for Tilde:

https://github.com/Umuzi-org/Tilde/tree/master/database/localhost

And you can look at the Tilde settings.py file here to see how we use environmental variables to set up database access:

https://github.com/Umuzi-org/Tilde/blob/master/backend/backend/settings.py

Instructions
For this introductory part of the project you’ll need to just get a foundation in place on which you can work.

Set up an empty Django project
Connect to a postgres db
Make sure you can create super users
