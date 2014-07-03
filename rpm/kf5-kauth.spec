# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-kauth

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 2 module to perform actions as privileged user
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kauth.yaml
Source101:  kf5-kauth-rpmlintrc
Patch0:     kauth-find-polkit-qt5.patch
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kcoreaddons-devel

%description
KAuth is a framework to let applications perform actions as a privileged user.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# kauth-find-polkit-qt5.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
%find_lang kauth5_qt --with-qt --all-name || :
# << install pre

# >> install post
# << install post

%files -f kauth5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Auth.so.*
%{_kf5_sysconfdir}/dbus-1/system.d/*
%{_qt5_plugindir}/kauth/helper/kauth_helper_plugin.so
%{_qt5_plugindir}/kauth/backend/kauth_backend_plugin.so
%{_kf5_datadir}/kf5/kauth/
%{_libexecdir}/kauth/kauth-policy-gen
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kauth_version.h
%{_kf5_includedir}/KAuth
%{_kf5_libdir}/libKF5Auth.so
%{_kf5_libdir}/cmake/KF5Auth
%{_datadir}/qt5/mkspecs/modules/qt_KAuth.pri
# >> files devel
# << files devel
