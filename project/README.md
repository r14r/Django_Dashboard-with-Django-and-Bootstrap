#!/usr/bin/env bash


PAGES="frontend
utilities/borders
utilities/others
utilities/colors
utilities/animations
components/buttons
components/cards
pages/tables
pages/password
pages/pagenotfound
pages/charts
pages/blank
pages/register
pages/login"


for PAGE in $PAGES
do
    echo $PAGE
    # mkdir apps/pages && python manage.py  startapp Pages apps/pages
done


exit

