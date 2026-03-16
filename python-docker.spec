%define module docker

Name:		python-docker
Version:	7.1.0
Release:	1
Summary:	A Python library for the Docker Engine API
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/docker/docker-py
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(packaging) >= 14.0
Requires:	python%{pyver}dist(websocket-client) >= 0.32.0
Recommends:	python%{pyver}dist(paramiko) >= 2.4.3

%description
A Python library for the Docker Engine API.

It lets you do anything the docker command does, but from within
Python apps – run containers, manage containers, manage Swarms, etc.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
