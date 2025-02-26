Name:           snake
Version:        1.0
Release:        1%{?dist}
Summary:        A simple Snake game
Group:          Games/Entertainment 

License:        GPLv3+
URL:            https://github.com/aeevs/MyGitProject/Lab3
Source0:        snake-1.0.tar

BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
Requires:       ncurses

%description
A simple Snake game implemented in C++.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 snake %{buildroot}/usr/local/bin/snake

%files
/usr/local/bin/snake

%changelog
* Thu Feb 26 2025 Alexey Evseev <aeevs.mail@ru> - 1.0-1
- Initial package.
