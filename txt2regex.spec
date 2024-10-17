Summary:	A program to generate regex
Name:		txt2regex
Version:	0.8
Release:	7
Group:		File tools
License:	GPLv2
URL:            https://www.aurelio.net/soft/txt2regex/
Source0:        http://txt2regex.sourceforge.net/%{name}-%{version}.tgz
BuildArch:	noarch
Requires:	bash

%description
^txt2regex$ is a Regular Expression "wizard", all written 
with bash2 builtins, that converts human sentences to 
RegExs. with a simple interface, you just answer to 
questions and build your own RegEx for a large variety of 
programs, like awk, ed, emacs, grep, perl, php, procmail, 
python, sed and vim. there are more than 20 supported 
programs. it's bash so download and run, no compilation needed.

%prep 

%setup -q

%build 

%make DESTDIR=%{buildroot}

%install
%makeinstall_std

install -d %{buildroot}%{_mandir}/man1
install -m0644 txt2regex.man %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc README README.japanese NEWS Changelog TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
