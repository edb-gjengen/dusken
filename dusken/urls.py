from django.conf.urls import url, include

from dusken.api import urls as api_urls
from dusken.views.email import EmailSubscriptions
from dusken.views.general import IndexView, HomeView, OrderDetailView, HomeVolunteerView
from dusken.views.membership import (MembershipPurchaseView, MembershipListView,
                                     MembershipActivateView, MembershipRenewView)
from dusken.views.orgunit import OrgUnitListView, OrgUnitDetailView, OrgUnitEditView
from dusken.views.user import (UserRegisterView, UserDetailView, UserDetailMeView, UserListView,
                               UserUpdateView, UserUpdateMeView,
                               UserEmailValidateView, UserEmailValidateSuccessView,
                               UserPhoneValidateView, UserPhoneValidateSuccessView)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home/$', HomeView.as_view(), name='home'),

    # User
    url(r'^me/$', UserDetailMeView.as_view(), name='user-detail-me'),
    url(r'^me/update/$', UserUpdateMeView.as_view(), name='user-update-me'),
    url(r'^users/(?P<slug>[0-9a-z-]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^users/(?P<slug>[0-9a-z-]+)/update/$', UserUpdateView.as_view(), name='user-update'),
    url(r'^users/$', UserListView.as_view(), name='user-list'),

    # User auth
    url(r'^register/$', UserRegisterView.as_view(), name='user-register'),
    url(r'^users/(?P<slug>[0-9a-z-]+)/validate_email/(?P<email_key>[0-9a-zA-Z-]+)$',
        UserEmailValidateView.as_view(),
        name='user-email-validate'),
    url(r'^users/validate_email_success/$', UserEmailValidateSuccessView.as_view(), name='user-email-validate-success'),
    url(r'^me/validate_phone/$', UserPhoneValidateView.as_view(), name='user-phone-validate'),
    url(r'^me/validate_phone_success/$', UserPhoneValidateSuccessView.as_view(),
        name='user-phone-validate-success'),

    # Membership
    url(r'^memberships/$', MembershipListView.as_view(), name='membership-list'),
    url(r'^memberships/purchase/$', MembershipPurchaseView.as_view(), name='membership-purchase'),
    url(r'^memberships/renew/$', MembershipRenewView.as_view(), name='membership-renew'),
    url(r'^memberships/activate/$', MembershipActivateView.as_view(), name='membership-activate'),

    url(r'^order/(?P<slug>[0-9a-z-]+)/$', OrderDetailView.as_view(), name='payment-detail'),

    # Volunteer
    url(r'^volunteer/$', HomeVolunteerView.as_view(), name='home-volunteer'),
    url(r'^orgunits/$', OrgUnitListView.as_view(), name='orgunit-list'),
    url(r'^orgunit/(?P<slug>[0-9a-z-]+)/$', OrgUnitDetailView.as_view(), name='orgunit-detail'),
    url(r'^orgunit/edit/(?P<slug>[0-9a-z-]+)/$', OrgUnitEditView.as_view(), name='orgunit-edit'),
    url(r'^orgunits/(?P<slug>[0-9a-z-]+)/$', OrgUnitDetailView.as_view(), name='orgunit-detail'),

    # Email
    url(r'email/subscriptions/$', EmailSubscriptions.as_view(), name='email-subscriptions')
]

urlpatterns += [
    url(r'api/', include(api_urls)),
]
