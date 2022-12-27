Name:		python-installer
Version:	0.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/i/installer/installer-%{version}.tar.gz
Summary:	A library for installing Python wheels.
URL:		https://pypi.org/project/installer/
License:	MIT
Group:		Development/Python
BuildRequires:	python-pip
BuildRequires:	python%{pyver}dist(flit-core)
BuildArch:	noarch

%description
A library for installing Python wheels.

%prep
%autosetup -p1 -n installer-%{version}

%build
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%{py_puresitedir}/installer
%{py_puresitedir}/installer*info
