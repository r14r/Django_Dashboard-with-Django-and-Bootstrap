from django.urls import path

from . import apps
from . import views

app_name = 'apps.pages.main'

urlpatterns = [
    path('', views.index, name='index',),

    path('/album', views.album, name='album',),
    path('/badges', views.badges, name='badges',),
    path('/blog', views.blog, name='blog',),
    path('/breadcrumbs', views.breadcrumbs, name='breadcrumbs',),
    path('/buttons', views.buttons, name='buttons',),
    path('/carousel', views.carousel, name='carousel',),
    path('/charts', views.charts, name='charts',),
    path('/cheatsheet', views.cheatsheet, name='cheatsheet',),
    path('/checkout', views.checkout, name='checkout',),
    path('/cover', views.cover, name='cover',),
    path('/dashboard', views.dashboard, name='dashboard',),
    path('/dropdowns', views.dropdowns, name='dropdowns',),
    path('/features', views.features, name='features',),
    path('/footers', views.footers, name='footers',),
    path('/grid', views.grid, name='grid',),
    path('/headers', views.headers, name='headers',),
    path('/heroes', views.heroes, name='heroes',),
    path('/jumbotron', views.jumbotron, name='jumbotron',),
    path('/jumbotrons', views.jumbotrons, name='jumbotrons',),
    path('/list-groups', views.list_groups, name='list-groups',),
    path('/login', views.login, name='login',),
    path('/main', views.main, name='main',),
    path('/masonry', views.masonry, name='masonry',),
    path('/modals', views.modals, name='modals',),
    path('/navbar-bottom', views.navbar_bottom, name='navbar-bottom',),
    path('/navbar-fixed', views.navbar_fixed, name='navbar-fixed',),
    path('/navbar-static', views.navbar_static, name='navbar-static',),
    path('/navbars', views.navbars, name='navbars',),
    path('/navbars-offcanvas', views.navbars_offcanvas, name='navbars-offcanvas',),
    path('/offcanvas', views.offcanvas, name='offcanvas',),
    path('/offcanvas-navbar', views.offcanvas_navbar, name='offcanvas-navbar',),
    path('/pagenotfound', views.pagenotfound, name='pagenotfound',),
    path('/password', views.password, name='password',),
    path('/pricing', views.pricing, name='pricing',),
    path('/product', views.product, name='product',),
    path('/register', views.register, name='register',),
    path('/sidebars', views.sidebars, name='sidebars',),
    path('/sign-in', views.sign_in, name='sign-in',),
    path('/starter-template', views.starter_template, name='starter-template',),
    path('/sticky-footer', views.sticky_footer, name='sticky-footer',),
    path('/sticky-footer-navbar', views.sticky_footer_navbar, name='sticky-footer-navbar',),



]
