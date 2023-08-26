#!/usr/local/bin/bash

PAGES="utilities/borders
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
    NAME="${PAGE##*/}"
    NAME="${NAME^}"
    echo "PAGE=$PAGE NAME=$NAME"

    FLDR="apps/$PAGE"

    echo "mkdir -p $FLDR && python manage.py  startapp $NAME $FLDR"
done


exit

