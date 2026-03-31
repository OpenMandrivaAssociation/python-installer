%define module installer

Name:		python-installer
Version:	1.0.0
Release:	1
Summary:	A library for installing Python wheels.
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/installer/
Source0:	https://files.pythonhosted.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
A library for installing Python wheels.

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
