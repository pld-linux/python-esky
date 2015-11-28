# %bcond_without	tests	# do not perform "make test"

%define 	module	esky
Summary:	An auto-update framework for frozen Python applications
Name:		python-%{module}
Version:	0.9.7
Release:	1
License:	ASL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/e/esky/esky-%{version}.tar.gz
# Source0-md5:	734e21aff103d78d80d24caca1b338ff
URL:		http://pypi.python.org/pypi/esky
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Esky is an auto-update framework for frozen Python applications. It
provides a simple API through which apps can find, fetch and install
updates, and a bootstrapping mechanism that keeps the app safe in the
face of failed or partial updates.

Esky is currently capable of freezing apps with py2exe, py2app,
cxfreeze and bbfreeze.

%prep
%setup -q -n esky-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/bdist_esky
%{py_sitescriptdir}/%{module}/bdist_esky/*.py[co]
%dir %{py_sitescriptdir}/%{module}/fstransact
%{py_sitescriptdir}/%{module}/fstransact/*.py[co]
%dir %{py_sitescriptdir}/%{module}/sudo
%{py_sitescriptdir}/%{module}/sudo/*.py[co]
%dir %{py_sitescriptdir}/%{module}/tests
%{py_sitescriptdir}/%{module}/tests/*.py[co]
%dir %{py_sitescriptdir}/%{module}/tests/eskytester
%{py_sitescriptdir}/%{module}/tests/eskytester/*.py[co]
%{py_sitescriptdir}/%{module}/tests/eskytester/*.txt
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}*.egg-info
%endif
