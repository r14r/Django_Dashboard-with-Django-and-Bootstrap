from django.shortcuts import render


def display_template(request, template, context={}):
    return render(request, f"{template}.html", context)


def index(request):
    return display_template(request, "main")


def album(request):
    return display_template(request, "album")


def badges(request):
    return display_template(request, "badges")


def blog(request):
    return display_template(request, "blog")


def breadcrumbs(request):
    return display_template(request, "breadcrumbs")


def buttons(request):
    return display_template(request, "buttons")


def carousel(request):
    return display_template(request, "carousel")


def charts(request):
    return display_template(request, "charts")


def cheatsheet(request):
    return display_template(request, "cheatsheet")


def checkout(request):
    return display_template(request, "checkout")


def cover(request):
    return display_template(request, "cover")


def dashboard(request):
    return display_template(request, "dashboard")


def dropdowns(request):
    return display_template(request, "dropdowns")


def features(request):
    return display_template(request, "features")


def footers(request):
    return display_template(request, "footers")


def grid(request):
    return display_template(request, "grid")


def headers(request):
    return display_template(request, "headers")


def heroes(request):
    return display_template(request, "heroes")


def jumbotron(request):
    return display_template(request, "jumbotron")


def jumbotrons(request):
    return display_template(request, "jumbotrons")


def list_groups(request):
    return display_template(request, "list-groups")


def login(request):
    return display_template(request, "login")


def main(request):
    return display_template(request, "main")


def masonry(request):
    return display_template(request, "masonry")


def modals(request):
    return display_template(request, "modals")


def navbar_bottom(request):
    return display_template(request, "navbar-bottom")


def navbar_fixed(request):
    return display_template(request, "navbar-fixed")


def navbar_static(request):
    return display_template(request, "navbar-static")


def navbars(request):
    return display_template(request, "navbars")


def navbars_offcanvas(request):
    return display_template(request, "navbars-offcanvas")


def offcanvas(request):
    return display_template(request, "offcanvas")


def offcanvas_navbar(request):
    return display_template(request, "offcanvas-navbar")


def pagenotfound(request):
    return display_template(request, "pagenotfound")


def password(request):
    return display_template(request, "password")


def pricing(request):
    return display_template(request, "pricing")


def product(request):
    return display_template(request, "product")


def register(request):
    return display_template(request, "register")


def sidebars(request):
    return display_template(request, "sidebars")


def sign_in(request):
    return display_template(request, "sign-in")


def starter_template(request):
    return display_template(request, "starter-template")


def sticky_footer(request):
    return display_template(request, "sticky-footer")


def sticky_footer_navbar(request):
    return display_template(request, "sticky-footer-navbar")
