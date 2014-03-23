%define		efl_ver		1.9.0
%define		ecore_ver	%{efl_ver}
%define		ecore_file_ver	1.8.0
%define		edje_ver	%{efl_ver}
%define		eina_ver	%{efl_ver}
%define		emotion_ver	%{efl_ver}
%define		eo_ver		%{efl_ver}
%define		evas_ver	%{efl_ver}
%define		elementary_ver	1.9.0
%define		py_dbus_ver	0.83.0

Summary:	Python bindings for Enlightenment Foundation Libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek EFL (Enlightenment Foundation Libraries)
Name:		python-efl
Version:	1.9.0
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/rel/bindings/python/%{name}-%{version}.tar.bz2
# Source0-md5:	4a37778c690cd9d673575416df060b55
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	python-dbus-devel >= %{py_dbus_ver}
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	ecore-file-devel >= %{ecore_file_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eina-devel >= %{eina_ver}
BuildRequires:	elementary-devel >= %{elementary_ver}
BuildRequires:	emotion-devel >= %{emotion_ver}
BuildRequires:	eo-devel >= %{eo_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	pkgconfig
# when using *.pyx sources, not pregenerated *.c
#BuildRequires:	python-Cython >= 0.17.0
BuildRequires:	python-Sphinx
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFL is a collection of libraries for handling many common tasks a
developer man have such as data structures, communication, rendering,
widgets and more. PYTHON-EFL are the Python bindings for EFL and
Elementary.

%description -l pl.UTF-8
EFL to zbiór bibliotek do obsługi wielu częstych zadań programisty,
takich jak struktury danych, komunikacja, renderowanie, widgety itp.
PYTHON-EFL to wiązania Pythona do bibliotek EFL i Elementary.

%package base
Summary:	Python bindings for Enlightenment Foundation Libraries - base common part
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek EFL - wspólna część podstawowa
Group:		Development/Languages/Python
Requires:	eina >= %{eina_ver}
Requires:	eo >= %{eina_ver}

%description base
Python bindings for Enlightenment Foundation Libraries - base common
part:
- Eo library binding
- efl.utils modules

%description base
Wiązania Pythona do bibliotek EFL (Enlightenment Foundation Libraries)
- wspólna część podstawowa:
- wiązanie do biblioteki Eo
- moduły efl.utils

%package examples
Summary:	Examples for PYTHON-EFL bindings
Summary(pl.UTF-8):	Przykłady do wiązań PYTHON-EFL
Group:		Development/Libraries
Requires:	python-dbus >= %{py_dbus_ver}
Requires:	python-e_dbus = %{version}-%{release}
Requires:	python-ecore = %{version}-%{release}
Requires:	python-edje = %{version}-%{release}
Requires:	python-elementary = %{version}-%{release}
Requires:	python-emotion = %{version}-%{release}
Requires:	python-evas = %{version}-%{release}

%description examples
Examples for PYTHON-EFL bindings.

%description examples -l pl.UTF-8
Przykłady do wiązań PYTHON-EFL.

%package -n python-e_dbus
Summary:	D-Bus Python integration for Ecore main loop
Summary(pl.UTF-8):	Integracja Python i DBus z główną pętlą Ecore
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	ecore >= %{ecore_ver}
Obsoletes:	python-e_dbus < 1.8.0

%description -n python-e_dbus
D-Bus Python integration for Ecore main loop. There is also e_dbus
API provided for compatibility with EFL 1.7.0 bindings.

%description -n python-e_dbus -l pl.UTF-8
Integracja Python i DBus z główną pętlą Ecore. Dołączone jest także
API e_dbus dla kompatybilności z wiązaniami EFL 1.7.0.

%package -n python-ecore
Summary:	Python bindings for Ecore library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ecore
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	ecore >= %{ecore_ver}
Requires:	ecore-file >= %{ecore_file_ver}
Obsoletes:	python-ecore-devel < 1.8.0
Obsoletes:	python-ecore-evas < 1.8.0
Obsoletes:	python-ecore-evas-devel < 1.8.0
Obsoletes:	python-ecore-file < 1.8.0
Obsoletes:	python-ecore-file-devel < 1.8.0
Obsoletes:	python-ecore-imf < 1.8.0
Obsoletes:	python-ecore-imf-devel < 1.8.0
Obsoletes:	python-ecore-x < 1.8.0
Obsoletes:	python-ecore-x-devel < 1.8.0

%description -n python-ecore
Python bindings for Ecore library.

%description -n python-ecore -l pl.UTF-8
Wiązania Pythona do biblioteki Ecore.

%package -n python-edje
Summary:	Python bindings for Edje library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Edje
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	edje-libs >= %{edje_ver}
Requires:	eina >= %{eina_ver}
Obsoletes:	python-edje-devel < 1.8.0

%description -n python-edje
Python bindings for Edje library.

%description -n python-edje -l pl.UTF-8
Wiązania Pythona do biblioteki Edje.

%package -n python-elementary
Summary:	Python bindings for Elementary library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Elementary
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	eina >= %{eina_ver}
Requires:	elementary-libs >= %{elementary_ver}
Requires:	evas >= %{evas_ver}
Obsoletes:	python-elementary-devel < 1.8.0

%description -n python-elementary
Python bindings for Elementary library.

%description -n python-elementary -l pl.UTF-8
Wiązania Pythona do biblioteki Elementary.

%package -n python-emotion
Summary:	Python bindings for Emotion library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Emotion
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	emotion >= %{emotion_ver}
Requires:	evas >= %{evas_ver}
Obsoletes:	python-emotion-devel < 1.8.0

%description -n python-emotion
Python bindings for Emotion library.

%description -n python-emotion -l pl.UTF-8
Wiązania Pythona do biblioteki Emotion.

%package -n python-evas
Summary:	Python bindings for Evas library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Evas
Group:		Development/Languages/Python
Requires:	%{name}-base = %{version}-%{release}
Requires:	eina >= %{eina_ver}
Requires:	evas >= %{evas_ver}
Obsoletes:	python-evas-devel < 1.8.0

%description -n python-evas
Python bindings for Evas library.

%description -n python-evas -l pl.UTF-8
Wiązania Pythona do biblioteki Evas.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' \
	examples/dbus/*.py \
	examples/elementary/*.py \
	examples/emotion/*.py \

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files base
%defattr(644,root,root,755)
%doc AUTHORS README changes.html
%dir %{py_sitedir}/efl
%{py_sitedir}/efl/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/efl/eo.so
%dir %{py_sitedir}/efl/utils
%{py_sitedir}/efl/utils/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/efl/utils/*.so
%{py_sitedir}/python_efl-%{version}-py*.egg-info

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/dbus
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/dbus/*.py
%dir %{_examplesdir}/%{name}-%{version}/elementary
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/elementary/test.py
%{_examplesdir}/%{name}-%{version}/elementary/test_*.py
%{_examplesdir}/%{name}-%{version}/elementary/*.edc
%{_examplesdir}/%{name}-%{version}/elementary/*.edj
%{_examplesdir}/%{name}-%{version}/elementary/images
%dir %{_examplesdir}/%{name}-%{version}/emotion
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/emotion/test_emotion.py
%{_examplesdir}/%{name}-%{version}/emotion/theme.edj

%files -n python-e_dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/efl/dbus_mainloop.so
%{py_sitedir}/e_dbus

%files -n python-ecore
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/efl/ecore.so
%{py_sitedir}/ecore

%files -n python-edje
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/efl/edje.so
%attr(755,root,root) %{py_sitedir}/efl/edje_edit.so
%{py_sitedir}/edje

%files -n python-elementary
%defattr(644,root,root,755)
%dir %{py_sitedir}/efl/elementary
%{py_sitedir}/efl/elementary/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/efl/elementary/*.so
%{py_sitedir}/elementary

%files -n python-emotion
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/efl/emotion.so
%{py_sitedir}/emotion

%files -n python-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/efl/evas.so
%{py_sitedir}/evas
