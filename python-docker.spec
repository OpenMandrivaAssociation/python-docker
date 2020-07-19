%bcond_without python3
%bcond_without tests

%bcond_without python2
%global srcname docker

Name:           python-%{srcname}
Version:	4.2.2
Release:	1
Summary:        A Python library for the Docker Engine API
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/d8/19/25ddbe30edff87274afb2b364c653c7f7bbdd515337700377f1adf0834c5/docker-4.2.2.tar.gz
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
