%define		py_dbus_ver	0.83.0

Summary:	Python bindings for Enlightenment Foundation Libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek EFL (Enlightenment Foundation Libraries)
Name:		python3-efl
Version:	1.26.1
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/rel/bindings/python/python-efl-%{version}.tar.xz
# Source0-md5:	7305bf32704d478330d2571bac5bdccd
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	python-dbus-devel >= %{py_dbus_ver}
BuildRequires:	efl-devel >= 1.27.0
BuildRequires:	pkgconfig
BuildRequires:	python3-Cython >= 0.19
BuildRequires:	python3-Sphinx
BuildRequires:	python3-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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

%package examples
Summary:	Examples for PYTHON-EFL bindings
Summary(pl.UTF-8):	Przykłady do wiązań PYTHON-EFL
Group:		Development/Libraries
Requires:	python-dbus >= %{py_dbus_ver}
Requires:	python3-efl = %{version}-%{release}

%description examples
Examples for PYTHON-EFL bindings.

%description examples -l pl.UTF-8
Przykłady do wiązań PYTHON-EFL.

%prep
%setup -q -n python-efl-%{version}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      examples/dbus/*.py \
      examples/ecore/con/*.py \
      examples/ecore/input/*.py \
      examples/ecore/x/*.py \
      examples/elementary/*.py \
      examples/emotion/*.py \
      examples/ethumb/*.py

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{py3_sitedir}/efl
%{py3_sitedir}/efl/*.py
%{py3_sitedir}/efl/__pycache__
%attr(755,root,root) %{py3_sitedir}/efl/*.so
%dir %{py3_sitedir}/efl/utils
%{py3_sitedir}/efl/utils/*.py
%{py3_sitedir}/efl/utils/__pycache__
%attr(755,root,root) %{py3_sitedir}/efl/utils/*.so
%{py3_sitedir}/python_efl-%{version}-py*.egg-info
%dir %{py3_sitedir}/efl/elementary
%{py3_sitedir}/efl/elementary/*.py
%{py3_sitedir}/efl/elementary/__pycache__
%attr(755,root,root) %{py3_sitedir}/efl/elementary/*.so

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/dbus
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/dbus/*.py
%dir %{_examplesdir}/%{name}-%{version}/ecore
%dir %{_examplesdir}/%{name}-%{version}/ecore/con
%{_examplesdir}/%{name}-%{version}/ecore/con/*.py
%dir %{_examplesdir}/%{name}-%{version}/ecore/input
%{_examplesdir}/%{name}-%{version}/ecore/input/*.py
%dir %{_examplesdir}/%{name}-%{version}/ecore/x
%{_examplesdir}/%{name}-%{version}/ecore/x/*.py
%dir %{_examplesdir}/%{name}-%{version}/elementary
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/elementary/test.py
%{_examplesdir}/%{name}-%{version}/elementary/test_*.py
%{_examplesdir}/%{name}-%{version}/elementary/*.edc
%{_examplesdir}/%{name}-%{version}/elementary/*.edj
%{_examplesdir}/%{name}-%{version}/elementary/images
%dir %{_examplesdir}/%{name}-%{version}/emotion
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/emotion/test_emotion.py
%{_examplesdir}/%{name}-%{version}/emotion/theme.edj
%dir %{_examplesdir}/%{name}-%{version}/ethumb
%{_examplesdir}/%{name}-%{version}/ethumb/*.py
