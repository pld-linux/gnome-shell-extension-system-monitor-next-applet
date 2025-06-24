Summary:	GNOME Shell System Monitor NEXT Extension
Name:		gnome-shell-extension-system-monitor-next-applet
Version:	3.27
Release:	2
# The entire source code is GPLv3+ except convenience.js, which is BSD
License:	GPL-3.0-or-later AND BSD-3-Clause
Source0:	https://github.com/mgalgs/gnome-shell-system-monitor-next-applet/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5dc0c451ec79403925eab992f8fb8ec3
Patch0:		no-schema-rebuild.patch
URL:		https://github.com/mgalgs/gnome-shell-system-monitor-next-applet
BuildRequires:	gettext
BuildArch:	noarch

%define		extuuid		system-monitor-next@paradoxxx.zero.gmail.com

%description
Display system information in gnome shell status bar, such as memory
usage, CPU usage, and network rate...

%prep
%setup -q -n gnome-shell-system-monitor-next-applet-%{version}
%patch -P0 -p1

%build
%{__make} BUILD_FOR_RPM=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	VERSION=%{version} \
	BUILD_FOR_RPM=1

# Install schema.
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{extuuid}/schemas
%{__cp} -p %{extuuid}/schemas/org.gnome.shell.extensions.system-monitor-next-applet.gschema.xml \
	$RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

# Install locale
%{__mv} $RPM_BUILD_ROOT%{_datadir}{/gnome-shell/extensions/%{extuuid},}/locale

%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/%{extuuid}/README

%{__mv} $RPM_BUILD_ROOT%{_localedir}/es{_ES,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/nl{_NL,}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md COPYING
%{_datadir}/gnome-shell/extensions/%{extuuid}
%{_datadir}/glib-2.0/schemas/*gschema.xml
