%bcond_without python3
%bcond_without tests

%bcond_without python2
%global srcname docker

Name:           python-%{srcname}
Version:	5.0.3
Release:	4
Summary:        A Python library for the Docker Engine API
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.4.0
Requires:       python-websocket-client >= 0.32.0
Requires:       python-docker-pycreds >= 0.2.1
Requires:       python-pyopenssl
Requires:       python-idna
Requires:       python-cryptography

BuildArch:      noarch

%description
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.

%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -fr docker.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
